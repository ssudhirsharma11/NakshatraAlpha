"""
Base class for market data providers.
"""

from abc import ABC, abstractmethod
from datetime import datetime

from src.market.market_dataset import MarketDataset
from src.market.timeframe import Timeframe


class BaseMarketProvider(ABC):

    @abstractmethod
    def download(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime,
    ) -> MarketDataset:
        """
        Download historical market data.
        """
        raise NotImplementedError