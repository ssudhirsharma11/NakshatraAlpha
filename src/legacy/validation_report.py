"""
Validation Report

Entry point for validating Nakshatra Alpha calculations.

Modes:
    - Single Hora
    - Single Day
    - Date Range
"""

from __future__ import annotations

from datetime import date, datetime

from src.research.validation_builder import ValidationBuilder
from src.research.console_formatter import ConsoleFormatter

# ==========================================================
# CONFIGURATION
# ==========================================================

# REPORT MODE
# "TIMESTAMP"
# "DAY"
# "RANGE"

REPORT_MODE = "DAY"

# Used when REPORT_MODE == "TIMESTAMP"
REPORT_TIMESTAMP = datetime(
    2026,
    7,
    1,
    10,
    30,
)

# Used when REPORT_MODE == "DAY"
REPORT_DATE = date(
    2026,
    7,
    1,
)

# Used when REPORT_MODE == "RANGE"
START_DATE = date(
    2026,
    7,
    1,
)

END_DATE = date(
    2026,
    7,
    31,
)

# Optional
# None = all horas
# 1..12 = only one hora
REPORT_HORA = None


def main() -> None:

    builder = ValidationBuilder()

    formatter = ConsoleFormatter()

    if REPORT_MODE == "TIMESTAMP":

        report = builder.build_timestamp(
            REPORT_TIMESTAMP
        )

    elif REPORT_MODE == "DAY":

        report = builder.build_day(
            REPORT_DATE,
            REPORT_HORA,
        )

    elif REPORT_MODE == "RANGE":

        report = builder.build_range(
            START_DATE,
            END_DATE,
            REPORT_HORA,
        )

    else:

        raise ValueError(
            f"Unknown REPORT_MODE: {REPORT_MODE}"
        )

    formatter.print(report)


if __name__ == "__main__":

    main()