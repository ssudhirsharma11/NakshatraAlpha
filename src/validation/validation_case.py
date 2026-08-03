"""
Validation Case

Represents one golden validation test case.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class ValidationCase:
    """
    One validation case loaded from CSV.
    """

    # ---------------------------------------------------------
    # Input
    # ---------------------------------------------------------

    timestamp: datetime

    latitude: float

    longitude: float

    # ---------------------------------------------------------
    # Expected Astrology
    # ---------------------------------------------------------

    expected_weekday: Optional[str] = None

    expected_hora: Optional[str] = None

    expected_tithi: Optional[str] = None

    expected_tithi_group: Optional[str] = None

    expected_tithi_lord: Optional[str] = None

    expected_paksha: Optional[str] = None

    expected_moon_nakshatra: Optional[str] = None

    expected_pada: Optional[int] = None

    expected_sun_sign: Optional[str] = None

    expected_moon_sign: Optional[str] = None

    expected_lagna: Optional[str] = None

    expected_saturn_from_sun: Optional[int] = None

    expected_saturn_from_moon: Optional[int] = None

    expected_sade_sati: Optional[bool] = None

    expected_sade_sati_phase: Optional[str] = None