"""
Dataset Validator

Validates the generated raw_dataset.csv before research begins.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class DatasetValidator:

    VALID_HORA_LORDS = {
        "SUN",
        "MOON",
        "MARS",
        "MERCURY",
        "JUPITER",
        "VENUS",
        "SATURN",
    }

    def validate(self, csv_file: str | Path) -> bool:

        csv_file = Path(csv_file)

        if not csv_file.exists():
            raise FileNotFoundError(csv_file)

        df = pd.read_csv(csv_file)

        print("\n" + "=" * 70)
        print("NAKSHATRA ALPHA DATA VALIDATION")
        print("=" * 70)

        passed = True

        # ---------------------------------------------------
        # Dataset
        # ---------------------------------------------------

        rows = len(df)
        cols = len(df.columns)
        duplicates = df.duplicated().sum()

        print("\nDATASET")
        print("-" * 40)

        print(f"Rows                    : {rows:,}")
        print(f"Columns                 : {cols}")
        print(f"Duplicate Rows          : {duplicates}")

        if rows == 0:
            print("❌ Dataset is empty")
            passed = False

        if duplicates > 0:
            print("❌ Duplicate rows detected")
            passed = False

        # ---------------------------------------------------
        # Hora
        # ---------------------------------------------------

        print("\nHORA")
        print("-" * 40)

        missing_number = df["hora_number"].isna().sum()
        missing_lord = df["hora_lord"].isna().sum()

        invalid_number = (~df["hora_number"].between(1, 24)).sum()

        invalid_lord = (
            ~df["hora_lord"].isin(self.VALID_HORA_LORDS)
        ).sum()

        print(f"Missing Hora Number     : {missing_number}")
        print(f"Missing Hora Lord       : {missing_lord}")
        print(f"Invalid Hora Number     : {invalid_number}")
        print(f"Invalid Hora Lord       : {invalid_lord}")

        if (
            missing_number > 0
            or missing_lord > 0
            or invalid_number > 0
            or invalid_lord > 0
        ):
            passed = False

        # ---------------------------------------------------
        # Market
        # ---------------------------------------------------

        print("\nMARKET")
        print("-" * 40)

        market_cols = [
            "open",
            "high",
            "low",
            "close",
        ]

        missing_market = df[market_cols].isna().sum().sum()

        invalid_ohlc = (
            (df["high"] < df["open"])
            | (df["high"] < df["close"])
            | (df["low"] > df["open"])
            | (df["low"] > df["close"])
        ).sum()

        negative_range = (df["trading_range"] < 0).sum()

        print(f"Missing OHLC            : {missing_market}")
        print(f"Invalid OHLC            : {invalid_ohlc}")
        print(f"Negative Range          : {negative_range}")

        if (
            missing_market > 0
            or invalid_ohlc > 0
            or negative_range > 0
        ):
            passed = False

        # ---------------------------------------------------
        # Time
        # ---------------------------------------------------

        print("\nTIME")
        print("-" * 40)

        start = pd.to_datetime(df["hora_start"])
        end = pd.to_datetime(df["hora_end"])

        invalid_duration = (end <= start).sum()

        print(f"Invalid Duration        : {invalid_duration}")

        if invalid_duration > 0:
            passed = False

        # ---------------------------------------------------
        # Hora Distribution
        # ---------------------------------------------------

        print("\nHORA DISTRIBUTION")
        print("-" * 40)

        hora_dist = (
            df["hora_lord"]
            .value_counts()
            .sort_index()
        )

        for lord, count in hora_dist.items():
            print(f"{lord:<10} {count}")

        # ---------------------------------------------------
        # Final Result
        # ---------------------------------------------------

        print("\n" + "=" * 70)

        if passed:
            print("✅ DATASET STATUS : PASSED")
        else:
            print("❌ DATASET STATUS : FAILED")

        print("=" * 70)

        return passed