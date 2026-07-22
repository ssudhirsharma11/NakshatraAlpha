"""
Nakshatra Position Model
"""

from dataclasses import dataclass

from src.models.nakshatra_enum import Nakshatra
from src.models.planet import Planet


@dataclass(frozen=True)
class NakshatraPosition:
    """
    Represents a planet's position within a Nakshatra.
    """

    planet: Planet

    nakshatra: Nakshatra

    number: int

    pada: int

    lord: Planet

    degrees_in_nakshatra: float

    degrees_remaining: float