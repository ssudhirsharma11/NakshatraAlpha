"""
Research Feature Set

Represents all astrology-derived features
for one timestamp.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureSet:

    moon_nakshatra: str

    moon_nakshatra_number: int

    sun_nakshatra: str

    sun_nakshatra_number: int

    tithi: str

    tithi_number: int

    paksha: str