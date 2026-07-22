"""
Generic OHLCV market bar.

Represents one candle/bar for any asset
at any timeframe.
"""

from dataclasses import dataclass
from datetime import datetime

from src.market.timeframe import Timeframe


@dataclass(frozen=True)
class OHLCVBar:

    symbol: str

    timeframe: Timeframe

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float | None = None