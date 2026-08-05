"""
Research Dataset Row

Represents one research observation.

One row = One Market Hora.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class ResearchDatasetRow:

    # =====================================================
    # Identity
    # =====================================================

    research_id: str

    trading_date: date

    weekday: str

    hora_number: int

    hora_lord: str

    # =====================================================
    # Panchang
    # =====================================================

    tithi: str

    tithi_group: str

    paksha: str

    nakshatra: str

    pada: int

    # =====================================================
    # Horoscope
    # =====================================================

    lagna: str

    moon_navamsha: str

    sun_navamsha: str

    # =====================================================
    # Saturn Analysis
    # =====================================================

    saturn_sign: str

    saturn_house_from_sun: int

    saturn_house_from_moon: int

    saturn_kendra_from_sun: bool

    saturn_kendra_from_moon: bool

    sade_sati: bool

    # =====================================================
    # Market
    # =====================================================

    market_open: float

    market_high: float

    market_low: float

    market_close: float

    return_percent: float

    trading_range: float

    candle_count: int

    # =====================================================
    # Export Helper
    # =====================================================

    def to_dict(self) -> dict:
        """
        Convert to dictionary for DataFrame creation.
        """

        return {
            "research_id": self.research_id,
            "trading_date": self.trading_date,
            "weekday": self.weekday,
            "hora_number": self.hora_number,
            "hora_lord": self.hora_lord,
            "tithi": self.tithi,
            "tithi_group": self.tithi_group,
            "paksha": self.paksha,
            "nakshatra": self.nakshatra,
            "pada": self.pada,
            "lagna": self.lagna,
            "moon_navamsha": self.moon_navamsha,
            "sun_navamsha": self.sun_navamsha,
            "saturn_sign": self.saturn_sign,
            "saturn_house_from_sun": self.saturn_house_from_sun,
            "saturn_house_from_moon": self.saturn_house_from_moon,
            "saturn_kendra_from_sun": self.saturn_kendra_from_sun,
            "saturn_kendra_from_moon": self.saturn_kendra_from_moon,
            "sade_sati": self.sade_sati,
            "market_open": self.market_open,
            "market_high": self.market_high,
            "market_low": self.market_low,
            "market_close": self.market_close,
            "return_percent": self.return_percent,
            "trading_range": self.trading_range,
            "candle_count": self.candle_count,
        }