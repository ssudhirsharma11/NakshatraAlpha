"""
Research Data Loader

Provides a simple interface for loading historical
market data used by the research engine.
"""

from __future__ import annotations

import pandas as pd

from src.services.market_data_service import (
    MarketDataService,
)


class DataLoader:
    """
    Thin wrapper around MarketDataService.

    Research modules should use this class instead of
    reading files directly.
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

    def has_data(
        self,
        trading_date,
    ) -> bool:

        return self.market_data.has_data(
            trading_date
        )