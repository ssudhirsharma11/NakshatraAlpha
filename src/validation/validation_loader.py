"""
Validation Loader

Loads validation cases from CSV files.
"""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from src.validation.validation_case import ValidationCase


class ValidationLoader:
    """
    Loads validation cases from CSV.
    """

    @staticmethod
    def load(csv_path: str | Path) -> list[ValidationCase]:

        csv_path = Path(csv_path)

        cases: list[ValidationCase] = []

        with csv_path.open(
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                timestamp = datetime.strptime(
                    f"{row['Date']} {row['Time']}",
                    "%Y-%m-%d %H:%M",
                ).replace(
                    tzinfo=ZoneInfo("Asia/Kolkata")
                )

                cases.append(
                    ValidationCase(
                        timestamp=timestamp,
                        latitude=float(row["Latitude"]),
                        longitude=float(row["Longitude"]),
                        expected_tithi=row.get("Tithi") or None,
                        expected_nakshatra=row.get("Nakshatra") or None,
                    )
                )

        return cases