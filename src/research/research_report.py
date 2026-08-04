"""
Research Report

Generate astrology + market reports.

Examples

Single Day
----------

python -m src.research.research_report ^
    --day 2026-07-17

Single Day - One Hora
---------------------

python -m src.research.research_report ^
    --day 2026-07-17 ^
    --hora 4

Date Range
----------

python -m src.research.research_report ^
    --start 2026-04-07 ^
    --end 2026-04-10

Date Range - One Hora
---------------------

python -m src.research.research_report ^
    --start 2026-04-07 ^
    --end 2026-04-10 ^
    --hora 6

Timestamp
---------

python -m src.research.research_report ^
    --timestamp "2026-07-17 10:30"
"""

from __future__ import annotations

import argparse

from datetime import date
from datetime import datetime

from src.research.report_printer import ReportPrinter
from src.research.research_builder import ResearchBuilder


# ==========================================================
# Helpers
# ==========================================================


def parse_date(value: str) -> date:

    return datetime.strptime(
        value,
        "%Y-%m-%d",
    ).date()


def parse_timestamp(value: str) -> datetime:

    return datetime.strptime(
        value,
        "%Y-%m-%d %H:%M",
    )


# ==========================================================
# CLI
# ==========================================================


def build_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        description="Nakshatra Alpha Research Report",
    )

    group = parser.add_mutually_exclusive_group(
        required=True,
    )

    group.add_argument(
        "--day",
        type=parse_date,
        help="Single trading day (YYYY-MM-DD)",
    )

    group.add_argument(
        "--timestamp",
        type=parse_timestamp,
        help="Timestamp (YYYY-MM-DD HH:MM)",
    )

    group.add_argument(
        "--start",
        type=parse_date,
        help="Start date for range",
    )

    parser.add_argument(
        "--end",
        type=parse_date,
        help="End date for range",
    )

    parser.add_argument(
        "--hora",
        type=int,
        choices=range(1, 13),
        help="Optional Hora number (1-12)",
    )

    return parser


# ==========================================================
# Main
# ==========================================================


def main():

    parser = build_parser()

    args = parser.parse_args()

    builder = ResearchBuilder()

    printer = ReportPrinter()

    # ------------------------------------------------------
    # Timestamp
    # ------------------------------------------------------

    if args.timestamp:

        rows = builder.build_timestamp(
            args.timestamp,
        )

    # ------------------------------------------------------
    # Day
    # ------------------------------------------------------

    elif args.day:

        rows = builder.build_day(
            args.day,
            args.hora,
        )

    # ------------------------------------------------------
    # Range
    # ------------------------------------------------------

    elif args.start:

        if args.end is None:

            parser.error(
                "--start requires --end"
            )

        rows = builder.build_range(
            args.start,
            args.end,
            args.hora,
        )

    else:

        parser.error(
            "No report type selected."
        )

    printer.print(rows)


if __name__ == "__main__":
    main()