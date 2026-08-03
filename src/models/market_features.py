"""
Market Features

Derived features calculated from OHLC data.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MarketFeatures:

    # -----------------------------
    # Raw
    # -----------------------------

    open: float
    high: float
    low: float
    close: float

    # -----------------------------
    # Absolute
    # -----------------------------

    body: float

    trading_range: float

    upper_wick: float

    lower_wick: float

    # -----------------------------
    # Percentages
    # -----------------------------

    return_pct: float

    range_pct: float

    body_pct: float

    upper_wick_pct: float

    lower_wick_pct: float

    close_position_pct: float

    open_position_pct: float

    # -----------------------------
    # Classification
    # -----------------------------

    direction: str

    strength: str

    high_volatility: bool

    low_volatility: bool