"""
research_inspector.py

NakshatraAlpha Research Inspector

Purpose
-------
Human-readable inspection tool used to verify every
astrological and market calculation for any date or
date range.

This is NOT a research engine.

It is a validation / auditing tool.

Author:
NakshatraAlpha
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict
from typing import List

import pandas as pd


# ==========================================================
# USER INPUT
# ==========================================================

START_DATE = "2026-07-01"

END_DATE = "2026-07-01"

EXPORT_CSV = True

EXPORT_EXCEL = True


# ==========================================================
# RESEARCH INSPECTOR
# ==========================================================

class ResearchInspector:

    REQUIRED_COLUMNS = [

        "date",

        "hora_number",
        "hora_lord",
        "hora_start",
        "hora_end",

        "weekday",

        "tithi",
        "paksha",

        "moon_nakshatra",
        "moon_sign",
        "moon_navamsha",

        "sun_sign",
        "sun_navamsha",

        "lagna_sign",
        "lagna_degree",

        "saturn_from_sun",
        "saturn_from_moon",
        "saturn_kendra_from_sun",
        "sade_sati",
        "sade_sati_phase",

        "open",
        "high",
        "low",
        "close",

        "return_pct",
        "trading_range",

        "direction",
        "strength",

        "candle_count",

        "sun_longitude",
        "moon_longitude",
    ]

    WEEKDAY_NAMES = {

        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    TITHI_LORDS = {

        1: "Sun",
        2: "Moon",
        3: "Mars",
        4: "Mercury",
        5: "Jupiter",
        6: "Venus",
        7: "Saturn",
        8: "Rahu",
        9: "Moon",
        10: "Mars",
        11: "Mercury",
        12: "Jupiter",
        13: "Venus",
        14: "Saturn",
        15: "Rahu",

        16: "Sun",
        17: "Moon",
        18: "Mars",
        19: "Mercury",
        20: "Jupiter",
        21: "Venus",
        22: "Saturn",
        23: "Rahu",
        24: "Moon",
        25: "Mars",
        26: "Mercury",
        27: "Jupiter",
        28: "Venus",
        29: "Saturn",
        30: "Rahu",
    }

    # ------------------------------------------------------
    # INIT
    # ------------------------------------------------------

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.dataset_file = (

            self.project_root
            / "data"
            / "research"
            / "research_dataset.csv"

        )

        self.output_dir = (

            self.project_root
            / "data"
            / "research"
            / "inspection"

        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.df = None

        self.filtered_df = None

    # ------------------------------------------------------
    # LOAD DATASET
    # ------------------------------------------------------

    def load_dataset(self):

        if not self.dataset_file.exists():

            raise FileNotFoundError(

                f"Dataset not found:\n{self.dataset_file}"

            )

        self.df = pd.read_csv(self.dataset_file)

        self.validate_dataset()

    # ------------------------------------------------------
    # VALIDATE
    # ------------------------------------------------------

    def validate_dataset(self):

        missing = []

        for column in self.REQUIRED_COLUMNS:

            if column not in self.df.columns:

                missing.append(column)

        if missing:

            raise ValueError(

                "Missing Columns\n\n"

                + "\n".join(missing)

            )

    # ------------------------------------------------------
    # FILTER DATE
    # ------------------------------------------------------

    def filter_dates(self):

        self.df["date"] = pd.to_datetime(

            self.df["date"]

        )

        start = pd.to_datetime(

            START_DATE

        )

        end = pd.to_datetime(

            END_DATE

        )

        self.filtered_df = self.df[

            (self.df["date"] >= start)

            &

            (self.df["date"] <= end)

        ].copy()

        if self.filtered_df.empty:

            raise ValueError(

                "No rows found for selected dates."

            )

        self.filtered_df.sort_values(

            [

                "date",

                "hora_number",

            ],

            inplace=True,

        )

    # ------------------------------------------------------
    # HELPERS
    # ------------------------------------------------------

    def get_tithi_lord(

        self,

        tithi_number,

    ):

        return self.TITHI_LORDS.get(

            int(tithi_number),

            "Unknown",

        )

    def weekday_name(

        self,

        weekday,

    ):

        try:

            return self.WEEKDAY_NAMES[

                int(weekday)

            ]

        except Exception:

            return str(weekday)

    @staticmethod
    def yes_no(value):

        if bool(value):

            return "YES"

        return "NO"

    @staticmethod
    def separator():

        print("=" * 70)

    @staticmethod
    def heading(title):

        print()

        print("-" * 70)

        print(title)

        print("-" * 70)
            # ------------------------------------------------------
    # DIRECTION VALIDATION
    # ------------------------------------------------------

    def validate_direction(self, row):

        expected = "Bullish"

        if row["close"] < row["open"]:
            expected = "Bearish"

        elif row["close"] == row["open"]:
            expected = "Neutral"

        status = "PASS"

        if str(expected).upper() != str(row["direction"]).upper():
            status = "FAIL"

        return expected, status

    # ------------------------------------------------------
    # STRENGTH VALIDATION
    # ------------------------------------------------------

    def validate_strength(self, row):

        """
        NOTE:
        This validation currently compares the stored value.

        Once we finalize the exact strength formula inside
        FeatureBuilder, this method should calculate the
        strength independently instead of trusting the dataset.
        """

        return row["strength"], "CHECK"

    # ------------------------------------------------------
    # PRINT SINGLE HORA
    # ------------------------------------------------------

    def print_hora(self, row):

        self.separator()

        print(
            f"{row['date'].strftime('%d-%b-%Y')}   "
            f"Hora {int(row['hora_number'])}"
        )

        print(
            f"{row['hora_start']}  -  {row['hora_end']}"
        )

        self.separator()

        # --------------------------------------------------
        # ASTROLOGY
        # --------------------------------------------------

        self.heading("ASTROLOGY")

        print(
            f"Hora Lord               : {row['hora_lord']}"
        )

        print(
            f"Weekday                 : "
            f"{self.weekday_name(row['weekday'])}"
        )

        print(
            f"Tithi                   : "
            f"{row['tithi']} "
            f"(Lord: {self.get_tithi_lord(row['tithi_number'])})"
        )

        print(
            f"Paksha                  : {row['paksha']}"
        )

        print(
            f"Moon Nakshatra          : "
            f"{row['moon_nakshatra']}"
        )

        print(
            f"Moon Sign               : "
            f"{row['moon_sign']}"
        )

        print(
            f"Moon Navamsha           : "
            f"{row['moon_navamsha']}"
        )

        print(
            f"Lagna                   : "
            f"{row['lagna_sign']} "
            f"({row['lagna_degree']:.2f}°)"
        )

        print(
            f"Sun Sign                : "
            f"{row['sun_sign']}"
        )

        print(
            f"Sun Navamsha            : "
            f"{row['sun_navamsha']}"
        )

        print(
            f"Sun Longitude           : "
            f"{row['sun_longitude']:.2f}°"
        )

        print(
            f"Moon Longitude          : "
            f"{row['moon_longitude']:.2f}°"
        )

        # --------------------------------------------------
        # SATURN
        # --------------------------------------------------

        self.heading("SATURN")

        print(
            f"Saturn from Sun         : "
            f"{row['saturn_from_sun']}"
        )

        print(
            f"Saturn from Moon        : "
            f"{row['saturn_from_moon']}"
        )

        print(
            f"Kendra (1/4/7/10)       : "
            f"{self.yes_no(row['saturn_kendra_from_sun'])}"
        )

        print(
            f"Sade Sati              : "
            f"{self.yes_no(row['sade_sati'])}"
        )

        print(
            f"Sade Sati Phase        : "
            f"{row['sade_sati_phase']}"
        )

        # --------------------------------------------------
        # MARKET
        # --------------------------------------------------

        self.heading("MARKET")

        print(f"Open                    : {row['open']:.2f}")
        print(f"High                    : {row['high']:.2f}")
        print(f"Low                     : {row['low']:.2f}")
        print(f"Close                   : {row['close']:.2f}")

        print()

        print(
            f"Trading Range           : "
            f"{row['trading_range']:.2f}"
        )

        print(
            f"Return %                : "
            f"{row['return_pct']:.2f}"
        )

        print(
            f"Candles Used            : "
            f"{int(row['candle_count'])}"
        )

        # --------------------------------------------------
        # VALIDATION
        # --------------------------------------------------

        self.heading("VALIDATION")

        expected_direction, direction_status = (
            self.validate_direction(row)
        )

        print(
            f"Direction Stored        : "
            f"{row['direction']}"
        )

        print(
            f"Direction Expected      : "
            f"{expected_direction}"
        )

        print(
            f"Direction Status        : "
            f"{direction_status}"
        )

        print()

        strength, strength_status = (
            self.validate_strength(row)
        )

        print(
            f"Strength Stored         : "
            f"{strength}"
        )

        print(
            f"Strength Validation     : "
            f"{strength_status}"
        )

        print()

        print(
            "Formula Check"
        )

        print(
            f"Close > Open            : "
            f"{row['close']:.2f} > {row['open']:.2f}"
        )

        print(
            f"Result                  : "
            f"{expected_direction}"
        )

        print()

    # ------------------------------------------------------
    # PRINT REPORT
    # ------------------------------------------------------

    def print_report(self):

        self.separator()

        print(
            "NAKSHATRAALPHA "
            "RESEARCH INSPECTOR"
        )

        self.separator()

        print(
            f"Start Date : {START_DATE}"
        )

        print(
            f"End Date   : {END_DATE}"
        )

        print(
            f"Rows        : "
            f"{len(self.filtered_df)}"
        )

        print()

        for _, row in self.filtered_df.iterrows():

            self.print_hora(row)
                # ------------------------------------------------------
    # EXPORT CSV
    # ------------------------------------------------------

    def export_csv(self):

        if not EXPORT_CSV:
            return

        output_file = (

            self.output_dir
            / (
                f"inspection_"
                f"{START_DATE}_"
                f"{END_DATE}.csv"
            )

        )

        self.filtered_df.to_csv(

            output_file,

            index=False,

        )

        print()

        print(
            f"[OK] CSV exported : {output_file.name}"
        )

    # ------------------------------------------------------
    # EXPORT EXCEL
    # ------------------------------------------------------

    def export_excel(self):

        if not EXPORT_EXCEL:
            return

        output_file = (

            self.output_dir
            / (
                f"inspection_"
                f"{START_DATE}_"
                f"{END_DATE}.xlsx"
            )

        )

        with pd.ExcelWriter(
            output_file,
            engine="openpyxl",
        ) as writer:

            self.filtered_df.to_excel(

                writer,

                sheet_name="Inspection",

                index=False,

            )

        print(
            f"[OK] Excel exported : {output_file.name}"
        )

    # ------------------------------------------------------
    # RUN
    # ------------------------------------------------------

    def run(self):

        self.load_dataset()

        self.filter_dates()

        self.print_report()

        self.export_csv()

        self.export_excel()

        self.separator()

        print(
            "INSPECTION COMPLETE"
        )

        self.separator()

        print()

        print(
            f"Rows Audited : {len(self.filtered_df)}"
        )

        print(
            f"Output Folder : {self.output_dir}"
        )

        print()

# ==========================================================
# MAIN
# ==========================================================

def main():

    try:

        inspector = ResearchInspector()

        inspector.run()

    except KeyboardInterrupt:

        print()

        print("Inspection cancelled.")

    except Exception as ex:

        print()

        print("=" * 70)

        print("ERROR")

        print("=" * 70)

        print(type(ex).__name__)

        print(ex)

        print()

if __name__ == "__main__":

    main()