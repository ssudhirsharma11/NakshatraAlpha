"""
Research Report

Entry point for generating astrology + market reports.

Supported modes

- TIMESTAMP
- DAY
- RANGE
"""

from __future__ import annotations

from datetime import date, datetime

from src.research.report_printer import ReportPrinter
from src.research.research_builder import ResearchBuilder


# ==========================================================
# CONFIGURATION
# ==========================================================

REPORT_MODE = "DAY"

# ----------------------------------------------------------
# Timestamp Mode
# ----------------------------------------------------------

REPORT_TIMESTAMP = datetime(
    2026,
    7,
    17,
    10,
    30,
)

# ----------------------------------------------------------
# Day Mode
# ----------------------------------------------------------

REPORT_DATE = date(
    2026,
    7,
    17,
)

# ----------------------------------------------------------
# Range Mode
# ----------------------------------------------------------

START_DATE = date(
    2026,
    7,
    13,
)

END_DATE = date(
    2026,
    7,
    17,
)

# ----------------------------------------------------------
# Optional
#
# None = All market horas
# 1-12 = Only one Hora
# ----------------------------------------------------------

REPORT_HORA = None


def main():

    builder = ResearchBuilder()

    printer = ReportPrinter()

    if REPORT_MODE == "TIMESTAMP":

        rows = builder.build_timestamp(
            REPORT_TIMESTAMP,
        )

    elif REPORT_MODE == "DAY":

        rows = builder.build_day(
            REPORT_DATE,
            REPORT_HORA,
        )

    elif REPORT_MODE == "RANGE":

        rows = builder.build_range(
            START_DATE,
            END_DATE,
            REPORT_HORA,
        )

    else:

        raise ValueError(
            f"Unsupported REPORT_MODE: {REPORT_MODE}"
        )

    printer.print(rows)


if __name__ == "__main__":
    main()