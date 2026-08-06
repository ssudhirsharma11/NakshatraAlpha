"""
Market Repository

Central access layer for all stored market datasets.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config.market_config import MARKET_DATA_DIR
from src.market.timeframe import Timeframe


class MarketRepository:

    def __init__(
        self,
        market_data_dir: Path = MARKET_DATA_DIR,
    ):

        self.market_data_dir = market_data_dir

    # ======================================================
    # Public
    # ======================================================

    def load(
        self,
        symbol: str,
        timeframe: Timeframe,
    ) -> pd.DataFrame:

        file = self.parquet_file(
            symbol,
            timeframe,
        )

        if not file.exists():

            raise FileNotFoundError(
                f"Dataset not found:\n{file}"
            )

        return pd.read_parquet(file)

    def exists(
        self,
        symbol: str,
        timeframe: Timeframe,
    ) -> bool:

        return self.parquet_file(
            symbol,
            timeframe,
        ).exists()

    def parquet_file(
        self,
        symbol: str,
        timeframe: Timeframe,
    ) -> Path:

        return (
            self.market_data_dir /
            f"{self._slug(symbol)}_{self._suffix(timeframe)}.parquet"
        )

    def csv_file(
        self,
        symbol: str,
        timeframe: Timeframe,
    ) -> Path:

        return (
            self.market_data_dir /
            f"{self._slug(symbol)}_{self._suffix(timeframe)}.csv"
        )

    # ======================================================
    # Helpers
    # ======================================================

    @staticmethod
    def _slug(
        symbol: str,
    ) -> str:

        return (
            symbol
            .lower()
            .replace("&", "and")
            .replace(" ", "_")
        )

    @staticmethod
    def _suffix(
        timeframe: Timeframe,
    ) -> str:

        mapping = {

            Timeframe.DAILY:
                "daily",

            Timeframe.HOUR_1:
                "60minute",

            Timeframe.MINUTE_30:
                "30minute",

            Timeframe.MINUTE_15:
                "15minute",

            Timeframe.MINUTE_5:
                "5minute",

            Timeframe.MINUTE_1:
                "1minute",

            Timeframe.WEEKLY:
                "weekly",
        }

        return mapping[timeframe]