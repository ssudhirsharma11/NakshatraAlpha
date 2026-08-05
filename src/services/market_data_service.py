"""
Market Data Service

Loads locally stored historical market data and provides
convenient access methods for research modules.

The service never communicates with Kite.
It only works with the locally downloaded Parquet dataset.
"""

from __future__ import annotations

from datetime import date, datetime
from functools import cached_property

import pandas as pd

from src.config.market_config import PARQUET_FILE


class MarketDataService:
    """
    Provides access to locally stored historical OHLC data.
    """

    REQUIRED_COLUMNS = (
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    )

    @cached_property
    def dataframe(self) -> pd.DataFrame:
        """
        Loads the historical market dataset.

        The dataframe is cached after the first read.
        """

        if not PARQUET_FILE.exists():

            raise FileNotFoundError(
                f"Market data file not found:\n{PARQUET_FILE}"
            )

        df = pd.read_parquet(
            PARQUET_FILE,
        )

        missing = [

            column

            for column in self.REQUIRED_COLUMNS

            if column not in df.columns

        ]

        if missing:

            raise ValueError(
                f"Missing required columns: {missing}"
            )

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        df.sort_values(
            "timestamp",
            inplace=True,
        )

        df.reset_index(
            drop=True,
            inplace=True,
        )

        return df

    # =====================================================
    # DATA ACCESS
    # =====================================================

    def get_all_data(
        self,
    ) -> pd.DataFrame:

        return self.dataframe.copy()

    def get_trading_day(
        self,
        trading_date: date,
    ) -> pd.DataFrame:

        df = self.dataframe

        mask = (
            df["timestamp"].dt.date
            == trading_date
        )

        return (
            df.loc[mask]
            .copy()
            .reset_index(drop=True)
        )

    def get_between(
        self,
        start: datetime,
        end: datetime,
    ) -> pd.DataFrame:

        df = self.dataframe

        mask = (
            (df["timestamp"] >= start)
            &
            (df["timestamp"] < end)
        )

        return (
            df.loc[mask]
            .copy()
            .reset_index(drop=True)
        )

    # =====================================================
    # INFORMATION
    # =====================================================

    def trading_days(
        self,
    ) -> list[date]:

        return sorted(

            self.dataframe[
                "timestamp"
            ]
            .dt.date
            .unique()
            .tolist()

        )

    def has_data(
        self,
        trading_date: date,
    ) -> bool:

        return not self.get_trading_day(
            trading_date
        ).empty

    def first_timestamp(
        self,
    ) -> datetime:

        return self.dataframe.iloc[0][
            "timestamp"
        ]

    def last_timestamp(
        self,
    ) -> datetime:

        return self.dataframe.iloc[-1][
            "timestamp"
        ]

    def total_candles(
        self,
    ) -> int:

        return len(
            self.dataframe
        )

    def total_trading_days(
        self,
    ) -> int:

        return len(
            self.trading_days()
        )