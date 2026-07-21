"""
Sprint 20B - Market Data Validator

Validates downloaded historical market data before
it is used for research and backtesting.
"""

from pathlib import Path

import pandas as pd


class DataValidator:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found.")

        self.df = pd.read_csv(self.file_path)

        self.df["date"] = pd.to_datetime(self.df["date"])

    def validate(self):

        print("\n==============================")
        print(" MARKET DATA VALIDATION REPORT ")
        print("==============================\n")

        self.check_total_rows()
        self.check_duplicates()
        self.check_missing_values()
        self.check_sorting()
        self.check_trading_days()
        self.check_daily_candle_count()

        print("\n==============================")
        print(" Validation Completed")
        print("==============================")

    def check_total_rows(self):

        print(f"Total Candles : {len(self.df)}")

    def check_duplicates(self):

        duplicates = self.df["date"].duplicated().sum()

        if duplicates == 0:
            print("✓ Duplicate Timestamps : PASS")
        else:
            print(f"✗ Duplicate Timestamps : {duplicates}")

    def check_missing_values(self):

        missing = self.df.isnull().sum().sum()

        if missing == 0:
            print("✓ Missing Values : PASS")
        else:
            print(f"✗ Missing Values : {missing}")

    def check_sorting(self):

        if self.df["date"].is_monotonic_increasing:
            print("✓ Chronological Order : PASS")
        else:
            print("✗ Chronological Order : FAILED")

    def check_trading_days(self):

        trading_days = self.df["date"].dt.date.nunique()

        print(f"Trading Days : {trading_days}")

    def check_daily_candle_count(self):

        daily_counts = self.df.groupby(self.df["date"].dt.date).size()

        expected = 75

        bad_days = daily_counts[daily_counts != expected]

        if bad_days.empty:
            print("✓ Daily Candle Count : PASS (75 candles/day)")
        else:
            print(f"✗ Days with Missing/Extra Candles : {len(bad_days)}")

            print("\nAffected Days:")

            print(bad_days)