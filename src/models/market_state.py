"""
Market State

Represents the complete astrological market state for one
research observation.

This object intentionally contains NO market prices.

It only describes the inferred market state derived from
the astrological model.

The actual OHLC outcome is stored separately and later used
for validation.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class MarketState:
    """
    Complete market state for one timestamp.
    """

    # ==========================================================
    # Identity
    # ==========================================================

    timestamp: object

    # ==========================================================
    # Macro Layer
    # ==========================================================

    macro_state: Optional[str] = None

    macro_score: float = 0.0

    jupiter_state: Optional[str] = None

    sun_state: Optional[str] = None

    saturn_state: Optional[str] = None

    # ==========================================================
    # Daily Bias
    # ==========================================================

    daily_state: Optional[str] = None

    daily_score: float = 0.0

    moon_phase_state: Optional[str] = None

    nakshatra_state: Optional[str] = None

    tithi_state: Optional[str] = None

    weekday_state: Optional[str] = None

    # ==========================================================
    # Intraday
    # ==========================================================

    intraday_state: Optional[str] = None

    intraday_score: float = 0.0

    hora_state: Optional[str] = None

    lagna_state: Optional[str] = None

    navamsha_state: Optional[str] = None

    saturn_relationship_state: Optional[str] = None

    # ==========================================================
    # Final
    # ==========================================================

    alignment_score: float = 0.0

    alignment_level: Optional[str] = None

    expected_market_state: Optional[str] = None

    confidence: float = 0.0

    # ==========================================================
    # Convenience
    # ==========================================================

    @property
    def bullish(self) -> bool:

        return (
            self.expected_market_state
            == "Bullish"
        )

    @property
    def bearish(self) -> bool:

        return (
            self.expected_market_state
            == "Bearish"
        )

    @property
    def neutral(self) -> bool:

        return (
            self.expected_market_state
            == "Neutral"
        )

    @property
    def conflict(self) -> bool:

        return (
            self.expected_market_state
            == "Conflict"
        )

    @property
    def aligned(self) -> bool:

        return (
            self.alignment_level
            == "High"
        )

    @property
    def partially_aligned(self) -> bool:

        return (
            self.alignment_level
            == "Medium"
        )

    @property
    def weak_alignment(self) -> bool:

        return (
            self.alignment_level
            == "Low"
        )

    def summary(self) -> dict:
        """
        Returns a concise summary.
        """

        return {

            "macro": self.macro_state,

            "daily": self.daily_state,

            "intraday": self.intraday_state,

            "alignment": self.alignment_level,

            "score": self.alignment_score,

            "expected": self.expected_market_state,

            "confidence": self.confidence,

        }