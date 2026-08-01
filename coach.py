#!/usr/bin/env python3
"""Single entry point. Normally you only need:  python3 coach.py sync"""

from __future__ import annotations

import sys

import garmin_pull
import garmin_report


def cmd_sync(args) -> int:
    api = garmin_pull.connect()
    garmin_pull.pull_all(
        api,
        activity_days=args.activity_days,
        wellness_days=args.wellness_days,
        refresh=args.refresh,
    )
    print()
    return garmin_report.main()


def cmd_report(_args) -> int:
    return garmin_report.main()


def cmd_login(_args) -> int:
    garmin_pull.connect()
    print("Connection works. Token saved - no password or MFA needed next time.")
    return 0


def main(argv: list[str]) -> int:
    import argparse

    p = argparse.ArgumentParser(
        prog="coach.py", description="Running coach - Garmin Connect data layer"
    )
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("sync", help="fetch data and build the report (default)")
    s.add_argument("--activity-days", type=int, default=365)
    s.add_argument("--wellness-days", type=int, default=90)
    s.add_argument("--refresh", action="store_true")
    s.set_defaults(func=cmd_sync)

    r = sub.add_parser("report", help="rebuild the report from cached data (offline)")
    r.set_defaults(func=cmd_report)

    lg = sub.add_parser("login", help="test the connection only")
    lg.set_defaults(func=cmd_login)

    args = p.parse_args(argv or ["sync"])
    if not hasattr(args, "func"):
        p.print_help()
        return 1

    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
