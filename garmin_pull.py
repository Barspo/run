#!/usr/bin/env python3
"""Pull raw training + wellness data from Garmin Connect into data/raw/.

Everything lands on disk as plain JSON so the report layer never has to touch
the network twice. Daily wellness is cached per-day, so a second run only
fetches the days it is missing.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
RAW = DATA / "raw"
DAILY = RAW / "daily"
TOKENS = ROOT / ".garmin_tokens"

# Garmin throttles hard. This pause between daily calls keeps us well under it.
CALL_DELAY = 0.35


# --------------------------------------------------------------------------
# auth
# --------------------------------------------------------------------------


def _prompt_mfa() -> str:
    return input("\n>> Enter the MFA code sent to you (6 digits): ").strip()


def connect(email: str | None = None, password: str | None = None) -> Garmin:
    """Log in, reusing cached tokens so MFA is only needed once per year."""
    TOKENS.mkdir(exist_ok=True)

    email = email or os.getenv("GARMIN_EMAIL")
    password = password or os.getenv("GARMIN_PASSWORD")

    api = Garmin(email=email, password=password, prompt_mfa=_prompt_mfa)

    try:
        api.login(tokenstore=str(TOKENS))
    except (GarminConnectAuthenticationError, FileNotFoundError):
        # No usable token cache -> we need credentials for a fresh login.
        if not email or not password:
            email = email or input("Garmin Connect email: ").strip()
            import getpass

            password = password or getpass.getpass(
                "Password (hidden while typing - just type it and press Enter): "
            )
            api = Garmin(email=email, password=password, prompt_mfa=_prompt_mfa)
        api.login(tokenstore=str(TOKENS))

    print(f"[OK] Logged in as {api.full_name or api.display_name}")
    return api


# --------------------------------------------------------------------------
# fetch helpers
# --------------------------------------------------------------------------


def safe(label: str, fn, *args, **kwargs):
    """Call a Garmin endpoint; never let one missing feature kill the run."""
    try:
        return fn(*args, **kwargs)
    except GarminConnectTooManyRequestsError:
        print(f"  ! {label}: rate limited by Garmin - waiting 60s")
        time.sleep(60)
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {label}: failed again ({type(exc).__name__}) - skipping")
            return None
    except Exception as exc:  # noqa: BLE001
        print(f"  - {label}: not available ({type(exc).__name__}) - skipping")
        return None


def _write(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")


# --------------------------------------------------------------------------
# the actual pull
# --------------------------------------------------------------------------


def pull_snapshot(api: Garmin, today: date) -> dict:
    """One-off metrics that describe the athlete right now."""
    print("\n[1/3] Profile, personal records and fitness metrics...")
    d = today.isoformat()
    year_ago = (today - timedelta(days=365)).isoformat()

    profile = safe("profile", api.get_user_profile) or {}
    settings = safe("settings", api.get_userprofile_settings) or {}

    # get_gear() wants the numeric profile PK, which lives under a different key
    # depending on which of the two profile endpoints answered.
    profile_pk = (
        profile.get("profileId")
        or profile.get("userProfilePk")
        or settings.get("id")
        or settings.get("userProfilePk")
    )

    snap = {
        "pulled_at": datetime.now().isoformat(timespec="seconds"),
        "display_name": api.display_name,
        "full_name": api.full_name,
        "unit_system": api.unit_system,
        "user_profile": profile,
        "profile_settings": settings,
        "race_predictions": safe("race predictions", api.get_race_predictions),
        "training_status": safe("training status", api.get_training_status, d),
        "max_metrics": safe("VO2max", api.get_max_metrics, d),
        "lactate_threshold": safe("lactate threshold", api.get_lactate_threshold),
        "personal_records": safe("personal records", api.get_personal_record),
        "endurance_score": safe("endurance score", api.get_endurance_score, year_ago, d),
        "hill_score": safe("hill score", api.get_hill_score, year_ago, d),
        "running_tolerance": safe(
            "running tolerance", api.get_running_tolerance, year_ago, d, "weekly"
        ),
        "devices": safe("devices", api.get_devices),
        "gear": safe("gear", api.get_gear, str(profile_pk)) if profile_pk else None,
        "weigh_ins": safe(
            "weight", api.get_weigh_ins, (today - timedelta(days=180)).isoformat(), d
        ),
    }
    return snap


def pull_activities(api: Garmin, today: date, days: int) -> list:
    """Every activity in the window, newest first."""
    print(f"\n[2/3] Activities (last {days} days)...")
    start = (today - timedelta(days=days)).isoformat()
    acts = safe("activities", api.get_activities_by_date, start, today.isoformat())
    acts = acts or []
    print(f"  found {len(acts)} activities")
    return acts


def pull_daily(api: Garmin, today: date, days: int, refresh: bool) -> int:
    """Per-day wellness: stats, sleep, HRV, training readiness. Cached per day."""
    print(f"\n[3/3] Sleep / HRV / resting HR (last {days} days)...")
    DAILY.mkdir(parents=True, exist_ok=True)
    fetched = 0

    for offset in range(days):
        day = today - timedelta(days=offset)
        d = day.isoformat()
        path = DAILY / f"{d}.json"

        # Yesterday and today can still change (sleep syncs late), so always
        # refresh the two most recent days.
        if path.exists() and not refresh and offset > 1:
            continue

        rec = {
            "date": d,
            "stats": safe(f"stats {d}", api.get_stats, d),
            "sleep": safe(f"sleep {d}", api.get_sleep_data, d),
            "hrv": safe(f"hrv {d}", api.get_hrv_data, d),
            "readiness": safe(f"readiness {d}", api.get_training_readiness, d),
        }
        _write(path, rec)
        fetched += 1

        if fetched % 10 == 0:
            print(f"  ...{fetched} days")
        time.sleep(CALL_DELAY)

    print(f"  downloaded {fetched} new days (the rest were cached)")
    return fetched


def pull_all(
    api: Garmin,
    activity_days: int = 365,
    wellness_days: int = 90,
    refresh: bool = False,
) -> None:
    today = date.today()

    _write(RAW / "snapshot.json", pull_snapshot(api, today))
    _write(RAW / "activities.json", pull_activities(api, today, activity_days))
    pull_daily(api, today, wellness_days, refresh)

    print(f"\n[OK] Data saved to {RAW}")


# --------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    import argparse

    p = argparse.ArgumentParser(description="משיכת נתונים מ-Garmin Connect")
    p.add_argument("--activity-days", type=int, default=365)
    p.add_argument("--wellness-days", type=int, default=90)
    p.add_argument(
        "--refresh",
        action="store_true",
        help="התעלם מהקאש ומשוך מחדש את כל הימים",
    )
    args = p.parse_args(argv)

    try:
        api = connect()
    except GarminConnectAuthenticationError as exc:
        print(f"\n[ERROR] Login failed: {exc}", file=sys.stderr)
        print("Check your email/password, and enter the MFA code if asked.", file=sys.stderr)
        return 1
    except GarminConnectConnectionError as exc:
        print(f"\n[ERROR] Connection problem with Garmin: {exc}", file=sys.stderr)
        return 1

    pull_all(
        api,
        activity_days=args.activity_days,
        wellness_days=args.wellness_days,
        refresh=args.refresh,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
