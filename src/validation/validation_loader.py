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
    Loads validation cases from a CSV file.
    """

    @staticmethod
    def _value(
        row: dict[str, str],
        column: str,
    ) -> str | None:
        """
        Returns a stripped value or None.
        """

        value = row.get(column)

        if value is None:
            return None

        value = value.strip()

        return value if value else None

    @staticmethod
    def _int(
        row: dict[str, str],
        column: str,
    ) -> int | None:
        """
        Reads an integer column.
        """

        value = ValidationLoader._value(
            row,
            column,
        )

        return int(value) if value else None

    @staticmethod
    def _bool(
        row: dict[str, str],
        column: str,
    ) -> bool | None:
        """
        Reads a boolean column.

        Accepted values

        True:
            TRUE
            YES
            1

        False:
            FALSE
            NO
            0
        """

        value = ValidationLoader._value(
            row,
            column,
        )

        if value is None:
            return None

        value = value.upper()

        if value in ("TRUE", "YES", "1"):
            return True

        if value in ("FALSE", "NO", "0"):
            return False

        raise ValueError(
            f"Invalid boolean '{value}' "
            f"for column '{column}'."
        )

    @staticmethod
    def load(
        csv_path: str | Path,
    ) -> list[ValidationCase]:

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
                    tzinfo=ZoneInfo(
                        "Asia/Kolkata"
                    )
                )

                cases.append(

                    ValidationCase(

                        # -----------------------------------------
                        # Input
                        # -----------------------------------------

                        timestamp=timestamp,

                        latitude=float(
                            row["Latitude"]
                        ),

                        longitude=float(
                            row["Longitude"]
                        ),

                        # -----------------------------------------
                        # Expected Results
                        # -----------------------------------------

                        expected_weekday=ValidationLoader._value(
                            row,
                            "Weekday",
                        ),

                        expected_hora=ValidationLoader._value(
                            row,
                            "Hora",
                        ),

                        expected_tithi=ValidationLoader._value(
                            row,
                            "Tithi",
                        ),

                        expected_tithi_group=ValidationLoader._value(
                            row,
                            "Tithi Group",
                        ),

                        expected_tithi_lord=ValidationLoader._value(
                            row,
                            "Tithi Lord",
                        ),

                        expected_paksha=ValidationLoader._value(
                            row,
                            "Paksha",
                        ),

                        expected_moon_nakshatra=ValidationLoader._value(
                            row,
                            "Moon Nakshatra",
                        ),

                        expected_pada=ValidationLoader._int(
                            row,
                            "Pada",
                        ),

                        expected_sun_sign=ValidationLoader._value(
                            row,
                            "Sun Sign",
                        ),

                        expected_moon_sign=ValidationLoader._value(
                            row,
                            "Moon Sign",
                        ),

                        expected_lagna=ValidationLoader._value(
                            row,
                            "Lagna",
                        ),

                        expected_saturn_from_sun=ValidationLoader._int(
                            row,
                            "Saturn From Sun",
                        ),

                        expected_saturn_from_moon=ValidationLoader._int(
                            row,
                            "Saturn From Moon",
                        ),

                        expected_sade_sati=ValidationLoader._bool(
                            row,
                            "Sade Sati",
                        ),

                        expected_sade_sati_phase=ValidationLoader._value(
                            row,
                            "Sade Sati Phase",
                        ),
                    )
                )

        return cases