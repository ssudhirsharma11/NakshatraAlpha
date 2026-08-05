"""
Market Loader

Loads validated historical market data
from the local Parquet dataset.
"""

from __future__ import annotations

import pandas as pd

from src.services.market_data_service import (
    MarketDataService,
)


class MarketLoader:
    """
    Thin wrapper around MarketDataService.

    Exists to isolate research modules from the
    underlying storage format.
    """

    def __init__(self):

        self.market_data = MarketDataService()

    def load(self) -> pd.DataFrame:
        """
        Returns the complete historical dataset.
        """

        return self.market_data.get_all_data()

    def trading_days(self):

        return self.market_data.trading_days()

    def trading_day(
        self,
        trading_date,
    ) -> pd.DataFrame:

        return self.market_data.get_trading_day(
            trading_date
        )

    def between(
        self,
        start,
        end,
    ) -> pd.DataFrame:

        return self.market_data.get_between(
            start,
            end,
        )