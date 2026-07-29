"""
Market Snapshot

Represents aggregated market statistics for a single
Hora period.

This object contains only market-derived information and
is intentionally independent of astrology.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MarketSnapshot:
    """
    Aggregated OHLC statistics for one Hora.
    """

    # ---------------------------------------------------------
    # OHLC
    # ---------------------------------------------------------

    open: float
    high: float
    low: float
    close: float

    # ---------------------------------------------------------
    # Derived Statistics
    # ---------------------------------------------------------

    up_move: float
    down_move: float
    trading_range: float

    candle_count: int

    # ---------------------------------------------------------
    # Convenience Properties
    # ---------------------------------------------------------

    @property
    def body(self) -> float:
        """
        Absolute body size.
        """
        return abs(self.close - self.open)

    @property
    def bullish(self) -> bool:
        """
        True if the Hora closed above its open.
        """
        return self.close > self.open

    @property
    def bearish(self) -> bool:
        """
        True if the Hora closed below its open.
        """
        return self.close < self.open

    @property
    def doji(self) -> bool:
        """
        True if the Hora closed exactly at its open.
        """
        return self.close == self.open