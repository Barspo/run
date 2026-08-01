#!/usr/bin/env python3
"""Turn the raw Garmin dump into one coach-readable Markdown briefing.

Reads only from data/raw/ — no network. Safe to re-run as often as you like.
"""

from __future__ import annotations

import json
import statistics
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
DAILY = RAW / "daily"
OUT = ROOT / "data" / "coach_report.md"

# Garmin's personal-record type ids. 1-7 are the running ones; anything else
# we print by id rather than guess at.
PR_TYPES = {
    1: "1 ק\"מ",
    2: "1 מייל",
    3: "5 ק\"מ",
    4: "10 ק\"מ",
    5: "חצי מרתון",
    6: "מרתון",
    7: "הריצה הארוכה ביותר",
}
DISTANCE_PRS = {7}


# --------------------------------------------------------------------------
# small formatting helpers
# --------------------------------------------------------------------------


def fnum(value):
    """Coerce to float, or None if the field isn't numeric.

    Garmin is inconsistent about types across endpoints and firmware
    versions, so nothing from the API is trusted to be a number.
    """
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def date_str(value) -> str:
    """Normalise Garmin's date encodings to YYYY-MM-DD.

    Depending on the endpoint a date arrives as an ISO string, an epoch in
    seconds, or an epoch in milliseconds.
    """
    if isinstance(value, str):
        return value[:10]
    ts = fnum(value)
    if ts is None:
        return ""
    if ts > 1e11:  # milliseconds
        ts /= 1000.0
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except (ValueError, OSError, OverflowError):
        return ""


def hhmmss(seconds) -> str:
    secs = fnum(seconds)
    if not secs:
        return "—"
    secs = int(round(secs))
    h, rem = divmod(secs, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def pace_str(dist_m, dur_s) -> str:
    """Pace as m:ss per km."""
    spk = pace_seconds(dist_m, dur_s)
    if spk is None:
        return "—"
    m, s = divmod(int(round(spk)), 60)
    return f"{m}:{s:02d}"


def pace_seconds(dist_m, dur_s):
    dist, dur = fnum(dist_m), fnum(dur_s)
    if not dist or not dur or dist < 100:
        return None
    return dur / (dist / 1000.0)


def km(meters) -> float:
    return round((fnum(meters) or 0) / 1000.0, 1)


def num(value, digits=1, suffix=""):
    if value is None:
        return "—"
    try:
        v = float(value)
    except (TypeError, ValueError):
        return str(value)
    return f"{round(v, digits):g}{suffix}"


def avg(values):
    vals = [x for x in (fnum(v) for v in values) if x is not None]
    return statistics.mean(vals) if vals else None


def load_json(path: Path, default=None):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def dig(obj, *keys, default=None):
    """Walk nested dicts without exploding on the first missing key."""
    cur = obj
    for k in keys:
        if isinstance(cur, list):
            cur = cur[0] if cur else None
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k)
    return default if cur is None else cur


def is_run(activity) -> bool:
    key = dig(activity, "activityType", "typeKey", default="") or ""
    return "run" in key.lower()


def act_date(activity):
    if not isinstance(activity, dict):
        return None
    stamp = date_str(activity.get("startTimeLocal") or activity.get("startTimeGMT"))
    if not stamp:
        return None
    try:
        return datetime.strptime(stamp, "%Y-%m-%d").date()
    except ValueError:
        return None


# --------------------------------------------------------------------------
# sections
# --------------------------------------------------------------------------


def section_profile(snap) -> list[str]:
    L = ["## 1. מי הרץ — נתוני בסיס מהשעון", ""]

    settings = snap.get("profile_settings") or {}
    user = settings.get("userData") or {}

    birth = date_str(user.get("birthDate"))
    age = None
    if birth:
        try:
            b = datetime.strptime(birth, "%Y-%m-%d").date()
            age = (date.today() - b).days // 365
        except ValueError:
            pass

    vo2 = dig(snap, "max_metrics", "generic", "vo2MaxPreciseValue") or dig(
        snap, "max_metrics", "generic", "vo2MaxValue"
    )
    if vo2 is None:
        vo2 = dig(snap, "training_status", "mostRecentVO2Max", "generic", "vo2MaxValue")

    lt_hr = dig(snap, "lactate_threshold", "speed_and_heart_rate", "heartRate")
    lt_speed = fnum(dig(snap, "lactate_threshold", "speed_and_heart_rate", "speed"))
    lt_pace = "—"
    if lt_speed:
        # Garmin stores threshold speed in m/s, but returns an implausible
        # magnitude when it hasn't gathered enough data to calibrate.
        spk = 1000 / lt_speed
        if 120 <= spk <= 600:  # 2:00-10:00 per km
            lt_pace = pace_str(1000, spk)

    weight_g = user.get("weight")
    weigh_ins = dig(snap, "weigh_ins", "dailyWeightSummaries", default=[])
    if isinstance(weigh_ins, list) and weigh_ins:
        latest = dig(weigh_ins[0], "latestWeight", "weight")
        weight_g = latest or weight_g

    rows = [
        ("שם", snap.get("full_name") or snap.get("display_name") or "—"),
        ("גיל", age or "—"),
        ("מין", user.get("gender") or "—"),
        ("גובה", num(user.get("height"), 0, " ס\"מ") if user.get("height") else "—"),
        ("משקל", num((fnum(weight_g) or 0) / 1000, 1, ' ק"ג') if fnum(weight_g) else "—"),
        ("VO2max ריצה", num(vo2)),
        ("דופק מקסימלי (מוגדר בשעון)", user.get("maxHeartRate") or "—"),
        ("דופק מנוחה (מוגדר בשעון)", user.get("restingHeartRate") or "—"),
        ("דופק סף חומצת חלב (LTHR)", lt_hr or "—"),
        ("קצב סף חומצת חלב", f"{lt_pace}/ק\"מ" if lt_pace != "—" else "—"),
        ("רמת פעילות מוצהרת", user.get("activityLevel") or "—"),
    ]
    L += ["| מדד | ערך |", "|---|---|"]
    L += [f"| {k} | {v} |" for k, v in rows]

    status = dig(snap, "training_status", "mostRecentTrainingStatus",
                 "latestTrainingStatusData", default={})
    if isinstance(status, dict) and status:
        first = next(iter(status.values()), {})
        if isinstance(first, dict):
            L += [
                "",
                f"- **סטטוס אימון נוכחי לפי גרמין:** {first.get('trainingStatusFeedbackPhrase') or first.get('trainingStatus') or '—'}",
            ]
            acute = first.get("acuteTrainingLoadDTO") or {}
            if acute:
                L.append(
                    f"- **עומס אקוטי:** {num(acute.get('acuteTrainingLoad'), 0)} "
                    f"(טווח מומלץ {num(acute.get('minTrainingLoad'), 0)}–{num(acute.get('maxTrainingLoad'), 0)})"
                )

    endurance = dig(snap, "endurance_score", "avg")
    if endurance:
        L.append(f"- **Endurance Score:** {num(endurance, 0)}")
    hill = dig(snap, "hill_score", "overallScore")
    if hill:
        L.append(f"- **Hill Score:** {num(hill, 0)}")

    return L + [""]


def section_predictions(snap) -> list[str]:
    preds = snap.get("race_predictions")
    if isinstance(preds, list):
        preds = preds[0] if preds else None
    if not isinstance(preds, dict):
        return []

    fields = [
        ("5 ק\"מ", "time5K", 5000),
        ("10 ק\"מ", "time10K", 10000),
        ("חצי מרתון", "timeHalfMarathon", 21097),
        ("מרתון", "timeMarathon", 42195),
    ]
    rows = []
    for label, key, dist in fields:
        secs = preds.get(key)
        if secs:
            rows.append(f"| {label} | {hhmmss(secs)} | {pace_str(dist, secs)}/ק\"מ |")

    if not rows:
        return []
    return [
        "## 2. תחזית זמנים לפי גרמין",
        "",
        "| מרחק | זמן חזוי | קצב |",
        "|---|---|---|",
        *rows,
        "",
        "> תחזיות גרמין נוטות להיות אופטימיות למרחקים ארוכים אם לא רצת אותם בפועל.",
        "",
    ]


def section_prs(snap) -> list[str]:
    prs = snap.get("personal_records")
    if not isinstance(prs, list) or not prs:
        return []

    rows = []
    for pr in prs:
        if not isinstance(pr, dict):
            continue
        tid = pr.get("typeId")
        label = PR_TYPES.get(tid)
        if not label:
            continue
        value = pr.get("value")
        when = date_str(
            pr.get("prStartTimeGmtFormatted")
            or pr.get("prStartTimeLocal")
            or pr.get("activityStartDateTimeLocal")
            or pr.get("prStartTimeGmt")
        )
        shown = f"{km(value)} ק\"מ" if tid in DISTANCE_PRS else hhmmss(value)
        rows.append(f"| {label} | {shown} | {when or '—'} |")

    if not rows:
        return []
    return ["## 3. שיאים אישיים", "", "| מרחק | שיא | תאריך |", "|---|---|---|", *rows, ""]


def section_weekly(runs, weeks=16) -> tuple[list[str], list[dict]]:
    """Weekly volume table + the aggregates other sections reuse."""
    today = date.today()
    this_monday = today - timedelta(days=today.weekday())

    buckets = defaultdict(list)
    for r in runs:
        d = act_date(r)
        if d:
            buckets[d - timedelta(days=d.weekday())].append(r)

    summary = []
    for i in range(weeks - 1, -1, -1):
        monday = this_monday - timedelta(weeks=i)
        acts = buckets.get(monday, [])
        dist = sum(fnum(a.get("distance")) or 0 for a in acts)
        dur = sum(fnum(a.get("duration")) or 0 for a in acts)
        elev = sum(fnum(a.get("elevationGain")) or 0 for a in acts)
        longest = max((fnum(a.get("distance")) or 0 for a in acts), default=0)
        load = sum(fnum(a.get("activityTrainingLoad")) or 0 for a in acts)
        summary.append(
            {
                "monday": monday,
                "runs": len(acts),
                "dist_m": dist,
                "dur_s": dur,
                "elev": elev,
                "longest_m": longest,
                "load": load,
                "acts": acts,
                "partial": monday == this_monday,
            }
        )

    L = [
        f"## 4. נפח שבועי — {weeks} השבועות האחרונים",
        "",
        "| שבוע (יום ב') | ריצות | ק\"מ | זמן | טיפוס | קצב ממוצע | ארוכה | % מהשבוע |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for w in summary:
        share = (
            f"{round(100 * w['longest_m'] / w['dist_m'])}%" if w["dist_m"] else "—"
        )
        # The current week is still running; don't let it read as a real drop.
        label = w["monday"].isoformat() + (" (חלקי)" if w["monday"] == this_monday else "")
        L.append(
            f"| {label} | {w['runs']} | {km(w['dist_m'])} | "
            f"{hhmmss(w['dur_s'])} | {num(w['elev'], 0, 'מ')} | "
            f"{pace_str(w['dist_m'], w['dur_s'])} | {km(w['longest_m'])} | {share} |"
        )

    # Averages use completed weeks only — the in-progress week would drag them down.
    recent = [w for w in summary[-9:-1] if w["dist_m"] > 0]
    if recent:
        L += [
            "",
            f"**ממוצע 8 שבועות מלאים אחרונים:** {round(sum(w['dist_m'] for w in recent) / len(recent) / 1000, 1)} ק\"מ/שבוע, "
            f"{round(sum(w['runs'] for w in recent) / len(recent), 1)} ריצות/שבוע",
        ]
    return L + [""], summary


def section_intensity(runs, days=56) -> list[str]:
    cutoff = date.today() - timedelta(days=days)
    zones = [0.0] * 5
    for r in runs:
        d = act_date(r)
        if not d or d < cutoff:
            continue
        for i in range(5):
            zones[i] += fnum(r.get(f"hrTimeInZone_{i + 1}")) or 0

    total = sum(zones)
    if total <= 0:
        return [
            "## 5. חלוקת עצימות",
            "",
            "אין נתוני אזורי דופק בפעילויות — כנראה רצת בלי מד דופק, או שהאזורים לא מוגדרים בשעון.",
            "",
        ]

    pct = [100 * z / total for z in zones]
    easy, moderate, hard = pct[0] + pct[1], pct[2], pct[3] + pct[4]

    L = [
        f"## 5. חלוקת עצימות — {days} ימים אחרונים",
        "",
        "| אזור | זמן | אחוז |",
        "|---|---|---|",
    ]
    for i, (z, p) in enumerate(zip(zones, pct), start=1):
        L.append(f"| Z{i} | {hhmmss(z)} | {round(p)}% |")

    L += [
        "",
        f"**קל (Z1+Z2): {round(easy)}% | בינוני (Z3): {round(moderate)}% | קשה (Z4+Z5): {round(hard)}%**",
        "",
    ]
    if easy < 75:
        L.append(
            f"> ⚠️ רק {round(easy)}% מהזמן בקל. המודל המקובל לרצי סיבולת הוא 80% קל / 20% קשה."
        )
    if moderate > 25:
        L.append(
            f"> ⚠️ {round(moderate)}% ב-Z3 (\"אזור אפור\") — מספיק קשה כדי לעייף, לא מספיק כדי לפתח."
        )
    return L + [""]


def section_key_sessions(runs, limit=12) -> list[str]:
    recent = sorted(
        [r for r in runs if act_date(r)], key=lambda r: act_date(r), reverse=True
    )[:limit]
    if not recent:
        return []

    L = [
        f"## 6. אימונים אחרונים ({len(recent)})",
        "",
        "| תאריך | שם | ק\"מ | זמן | קצב | דופק ממוצע/מקס | TE אירובי/אנאירובי | קדנס |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in recent:
        L.append(
            f"| {act_date(r).isoformat()} | {(r.get('activityName') or '—')[:28]} | "
            f"{km(r.get('distance'))} | {hhmmss(r.get('duration'))} | "
            f"{pace_str(r.get('distance'), r.get('duration'))} | "
            f"{num(r.get('averageHR'), 0)}/{num(r.get('maxHR'), 0)} | "
            f"{num(r.get('aerobicTrainingEffect'))}/{num(r.get('anaerobicTrainingEffect'))} | "
            f"{num(r.get('averageRunningCadenceInStepsPerMinute'), 0)} |"
        )

    # Fastest sustained efforts in the window - a rough proxy for current form.
    scored = [
        (pace_seconds(r.get("distance"), r.get("duration")), r)
        for r in runs
        if (fnum(r.get("distance")) or 0) >= 3000 and act_date(r)
    ]
    scored = sorted([s for s in scored if s[0]], key=lambda x: x[0])[:5]
    if scored:
        L += [
            "",
            "**5 הריצות המהירות (3 ק\"מ+) בחלון כולו:**",
            "",
            "| תאריך | ק\"מ | קצב | דופק ממוצע |",
            "|---|---|---|---|",
        ]
        for spk, r in scored:
            L.append(
                f"| {act_date(r).isoformat()} | {km(r.get('distance'))} | "
                f"{pace_str(r.get('distance'), r.get('duration'))} | {num(r.get('averageHR'), 0)} |"
            )

    return L + [""]


def section_form(runs, days=90) -> list[str]:
    """Running dynamics — only meaningful if the watch/strap reports them."""
    cutoff = date.today() - timedelta(days=days)
    window = [r for r in runs if (d := act_date(r)) and d >= cutoff]
    if not window:
        return []

    metrics = [
        ("קדנס (צעדים/דקה)", "averageRunningCadenceInStepsPerMinute", 0),
        ("אורך צעד (ס\"מ)", "avgStrideLength", 0),
        ("זמן מגע עם הקרקע (מ\"ש)", "avgGroundContactTime", 0),
        ("תנודה אנכית (ס\"מ)", "avgVerticalOscillation", 1),
        ("יחס אנכי (%)", "avgVerticalRatio", 1),
    ]
    rows = []
    for label, key, digits in metrics:
        m = avg([r.get(key) for r in window])
        if m is not None:
            rows.append(f"| {label} | {num(m, digits)} |")

    if not rows:
        return []
    return [
        f"## 7. מכניקת ריצה — ממוצע {days} ימים",
        "",
        "| מדד | ממוצע |",
        "|---|---|",
        *rows,
        "",
    ]


def load_daily() -> list[dict]:
    if not DAILY.exists():
        return []
    out = []
    for path in sorted(DAILY.glob("*.json")):
        rec = load_json(path)
        if rec:
            out.append(rec)
    return out


def section_sleep(daily) -> list[str]:
    rows = []
    for rec in daily:
        dto = dig(rec, "sleep", "dailySleepDTO", default={})
        if not isinstance(dto, dict) or not dto.get("sleepTimeSeconds"):
            continue
        start_ms = fnum(dto.get("sleepStartTimestampLocal"))
        bedtime = None
        if start_ms:
            try:
                t = datetime.fromtimestamp(start_ms / 1000)
                # Fold past-midnight bedtimes onto a continuous scale.
                bedtime = t.hour * 60 + t.minute
                if bedtime < 12 * 60:
                    bedtime += 24 * 60
            except (ValueError, OSError, TypeError):
                pass
        rows.append(
            {
                "date": rec["date"],
                "total": dto.get("sleepTimeSeconds"),
                "deep": dto.get("deepSleepSeconds"),
                "rem": dto.get("remSleepSeconds"),
                "light": dto.get("lightSleepSeconds"),
                "awake": dto.get("awakeSleepSeconds"),
                "score": dig(dto, "sleepScores", "overall", "value"),
                "bedtime": bedtime,
            }
        )

    if not rows:
        return ["## 8. שינה", "", "אין נתוני שינה בחלון שנמשך.", ""]

    def window(n):
        # n nights inclusive of today, so n-1 days back.
        cutoff = (date.today() - timedelta(days=n - 1)).isoformat()
        return [r for r in rows if r["date"] >= cutoff]

    L = ["## 8. שינה", "", "| חלון | לילות | שינה ממוצעת | עמוק | REM | ציון |", "|---|---|---|---|---|---|"]
    for n, label in ((7, "7 ימים"), (30, "30 ימים"), (90, "90 ימים")):
        w = window(n)
        if not w:
            continue
        L.append(
            f"| {label} | {len(w)} | {hhmmss(avg([r['total'] for r in w]))} | "
            f"{hhmmss(avg([r['deep'] for r in w]))} | {hhmmss(avg([r['rem'] for r in w]))} | "
            f"{num(avg([r['score'] for r in w]), 0)} |"
        )

    bedtimes = [r["bedtime"] for r in window(30) if r["bedtime"]]
    if len(bedtimes) >= 5:
        mean_bt = statistics.mean(bedtimes)
        sd = statistics.pstdev(bedtimes)
        h, m = divmod(int(mean_bt) % (24 * 60), 60)
        L += [
            "",
            f"**שעת שינה ממוצעת (30 יום):** {h:02d}:{m:02d} | **סטיית תקן:** {round(sd)} דקות",
        ]
        if sd > 60:
            L.append("> ⚠️ שעות השינה מאוד לא עקביות. עקביות משפיעה על ההתאוששות כמעט כמו משך השינה.")

    thirty = window(30)
    if thirty:
        mean_sleep = avg([r["total"] for r in thirty]) or 0
        if mean_sleep < 7 * 3600:
            L.append("")
            L.append(
                f"> ⚠️ ממוצע {hhmmss(mean_sleep)} שינה בלילה. מתחת ל-7 שעות מגדיל סיכון לפציעה ופוגע בהסתגלות לאימון."
            )
    return L + [""]


def section_recovery(daily) -> list[str]:
    hrv, rhr, stress, bb, readiness = [], [], [], [], []
    hrv_status = defaultdict(int)

    for rec in daily:
        d = rec["date"]
        v = fnum(dig(rec, "hrv", "hrvSummary", "lastNightAvg"))
        if v:
            hrv.append((d, v))
        st = dig(rec, "hrv", "hrvSummary", "status")
        if st:
            hrv_status[st] += 1

        r = fnum(dig(rec, "stats", "restingHeartRate"))
        if r and 30 <= r <= 85:
            rhr.append((d, r))
        s = fnum(dig(rec, "stats", "averageStressLevel"))
        if s and s > 0:
            stress.append((d, s))
        b = fnum(dig(rec, "stats", "bodyBatteryMostValue"))
        if b:
            bb.append((d, b))
        rd = fnum(dig(rec, "readiness", "score"))
        if rd:
            readiness.append((d, rd))

    def windowed(series, n):
        cutoff = (date.today() - timedelta(days=n - 1)).isoformat()
        return [v for d, v in series if d >= cutoff]

    L = [
        "## 9. התאוששות — HRV, דופק מנוחה, סטרס",
        "",
        "| מדד | 7 ימים | 28 ימים | מגמה |",
        "|---|---|---|---|",
    ]
    named = [
        ("HRV לילי (ms)", hrv, 0, "up_good"),
        ("דופק מנוחה", rhr, 0, "down_good"),
        ("סטרס ממוצע", stress, 0, "down_good"),
        ("Body Battery מקס", bb, 0, "up_good"),
        ("Training Readiness", readiness, 0, "up_good"),
    ]
    for label, series, digits, direction in named:
        w7, w28 = windowed(series, 7), windowed(series, 28)
        if not w7 or not w28:
            continue
        a7, a28 = statistics.mean(w7), statistics.mean(w28)
        delta = a7 - a28
        good = delta > 0 if direction == "up_good" else delta < 0
        arrow = "—" if abs(delta) < 0.5 else ("↑" if delta > 0 else "↓")
        mark = "" if abs(delta) < 0.5 else (" ✅" if good else " ⚠️")
        L.append(
            f"| {label} | {num(a7, digits)} | {num(a28, digits)} | {arrow} {num(delta, 1)}{mark} |"
        )

    if hrv_status:
        total = sum(hrv_status.values())
        parts = ", ".join(f"{k}: {round(100 * v / total)}%" for k, v in hrv_status.items())
        L += ["", f"**התפלגות סטטוס HRV:** {parts}"]

    base_low = None
    for rec in reversed(daily):
        base_low = dig(rec, "hrv", "hrvSummary", "baseline", "balancedLow")
        base_high = dig(rec, "hrv", "hrvSummary", "baseline", "balancedUpper")
        if base_low:
            L.append(f"**טווח HRV מאוזן אישי:** {num(base_low, 0)}–{num(base_high, 0)} ms")
            break

    return L + [""]


def section_data_quality(daily) -> list[str]:
    """Say plainly which metrics are missing or untrustworthy."""
    total = len(daily)
    if not total:
        return []

    sleep_days = sum(
        1 for r in daily if dig(r, "sleep", "dailySleepDTO", "sleepTimeSeconds")
    )
    hrv_days = sum(1 for r in daily if dig(r, "hrv", "hrvSummary", "lastNightAvg"))
    rhr = [fnum(dig(r, "stats", "restingHeartRate")) for r in daily]
    rhr = [v for v in rhr if v]
    bogus = [v for v in rhr if v > 85]

    notes = []
    if sleep_days / total < 0.3:
        notes.append(
            f"**שינה:** נתונים ב-{sleep_days} מתוך {total} לילות — השעון לא נלבש בשינה."
        )
    if hrv_days / total < 0.3:
        notes.append(
            f"**HRV:** נתונים ב-{hrv_days} מתוך {total} ימים — אין מדידה לילית."
        )
    if rhr and len(bogus) / len(rhr) > 0.5:
        notes.append(
            "**דופק מנוחה:** מעל 85 ברוב הימים — זה דופק בזמן פעילות, לא דופק מנוחה. "
            "הערכים האלה סוננו מהדוח."
        )
    if not notes:
        return []

    return [
        "## 0. איכות הנתונים — מה לא לסמוך עליו",
        "",
        *[f"- ⚠️ {n}" for n in notes],
        "",
        "> המדדים האלה הם מערכת ההתראה המוקדמת לעייפות יתר ולפציעה.",
        "> בלעדיהם התמונה חלקית.",
        "",
    ]


def section_flags(weekly, daily, runs) -> list[str]:
    flags = []

    # Every check below reasons about completed weeks. The in-progress week is
    # always short by definition and would fire false alarms on every metric.
    done = [w for w in weekly if not w["partial"]]
    recent = done[-8:]

    # Volume ramp - the classic injury precursor.
    active = [w for w in done if w["dist_m"] > 0]
    for prev, cur in zip(active, active[1:]):
        if prev["dist_m"] >= 10000:
            jump = 100 * (cur["dist_m"] - prev["dist_m"]) / prev["dist_m"]
            if jump > 30:
                flags.append(
                    f"קפיצת נפח של {round(jump)}% בשבוע של {cur['monday']} "
                    f"({km(prev['dist_m'])} → {km(cur['dist_m'])} ק\"מ) — מעל כלל ה-10%."
                )

    # Long run swallowing the week.
    for w in recent:
        if w["dist_m"] > 5000 and w["longest_m"] / w["dist_m"] > 0.45:
            flags.append(
                f"בשבוע של {w['monday']} הריצה הארוכה הייתה {round(100 * w['longest_m'] / w['dist_m'])}% "
                "מהנפח השבועי — מומלץ עד ~35%."
            )

    # Consecutive zero weeks in the recent block.
    zero_streak = 0
    for w in recent:
        zero_streak = zero_streak + 1 if w["runs"] == 0 else 0
    if zero_streak >= 2:
        flags.append(f"{zero_streak} שבועות מלאים אחרונים ללא ריצות כלל.")

    # Sparse weeks are a consistency problem, not a volume one.
    sparse = [w for w in recent if 0 < w["runs"] <= 2]
    if len(sparse) >= 4:
        flags.append(
            f"{len(sparse)} מתוך {len(recent)} השבועות המלאים האחרונים עם 2 ריצות או פחות — "
            "תדירות נמוכה מדי לשיפור."
        )

    if not flags:
        return ["## 10. דגלים אדומים", "", "לא זוהו דגלים אוטומטיים בחלון הנוכחי. ✅", ""]

    return ["## 10. דגלים אדומים (זוהו אוטומטית)", "", *[f"- {flag}" for flag in flags], ""]


# --------------------------------------------------------------------------


def build() -> str:
    snap = load_json(RAW / "snapshot.json", {}) or {}
    activities = load_json(RAW / "activities.json", []) or []
    daily = load_daily()
    runs = [a for a in activities if is_run(a)]

    other = len(activities) - len(runs)
    dates = [d for d in (act_date(a) for a in activities) if d]

    header = [
        "# דוח מאמן — נתוני Garmin",
        "",
        f"**נוצר:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ",
        f"**חלון פעילויות:** {min(dates) if dates else '—'} → {max(dates) if dates else '—'}  ",
        f"**ריצות:** {len(runs)} | **פעילויות אחרות:** {other} | **ימי בריאות:** {len(daily)}",
        "",
        "> העתק את כל הקובץ הזה לצ'אט עם המאמן.",
        "",
        "---",
        "",
    ]

    weekly_lines, weekly = section_weekly(runs)

    parts = [
        header,
        section_data_quality(daily),
        section_profile(snap),
        section_predictions(snap),
        section_prs(snap),
        weekly_lines,
        section_intensity(runs),
        section_key_sessions(runs),
        section_form(runs),
        section_sleep(daily),
        section_recovery(daily),
        section_flags(weekly, daily, runs),
    ]
    return "\n".join(line for part in parts for line in part)


def main() -> int:
    if not (RAW / "activities.json").exists():
        print("No data found. Run the sync first.")
        return 1

    text = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print(f"[OK] Report written to {OUT}")
    print(f"     {len(text.splitlines())} lines. Open it, copy all, paste into the chat.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
