"""
Market Data Service

Loads locally stored historical market data and provides
convenient access methods for research modules.

The service intentionally does NOT communicate with Kite.
It only works with downloaded historical CSV data.
"""

from __future__ import annotations

from datetime import date, datetime
from functools import cached_property

import pandas as pd

from src.config.research_config import MARKET_DATA_FILE


class MarketDataService:
    """
    Provides access to locally stored historical OHLC data.
    """

    REQUIRED_COLUMNS = (
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume",
    )

    @cached_property
    def dataframe(self) -> pd.DataFrame:
        """
        Loads the historical market data.

        The dataframe is cached after the first read.
        """

        if not MARKET_DATA_FILE.exists():
            raise FileNotFoundError(
                f"Market data file not found:\n{MARKET_DATA_FILE}"
            )

        df = pd.read_csv(
            MARKET_DATA_FILE,
            parse_dates=["date"],
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

        df = df.sort_values("date").reset_index(drop=True)

        return df

    def get_all_data(self) -> pd.DataFrame:
        """
        Returns the complete historical dataset.
        """

        return self.dataframe.copy()

    def get_trading_day(
        self,
        trading_date: date,
    ) -> pd.DataFrame:
        """
        Returns all candles for one trading day.
        """

        df = self.dataframe

        mask = (
            df["date"].dt.date == trading_date
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
        """
        Returns candles whose timestamps fall within
        the supplied interval.

        Start is inclusive.
        End is exclusive.
        """

        df = self.dataframe

        mask = (
            (df["date"] >= start)
            &
            (df["date"] < end)
        )

        return (
            df.loc[mask]
            .copy()
            .reset_index(drop=True)
        )

    def trading_days(self) -> list[date]:
        """
        Returns all unique trading dates.
        """

        return sorted(
            self.dataframe["date"]
            .dt.date
            .unique()
            .tolist()
        )

    def has_data(
        self,
        trading_date: date,
    ) -> bool:
        """
        Returns True if market data exists for
        the supplied trading day.
        """

        return not self.get_trading_day(
            trading_date
        ).empty