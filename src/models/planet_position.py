"""
Planet Position Model

Represents the complete position of a planet
at a specific instant in time.

This is the canonical planetary object used
throughout the astrology engine.
"""

from dataclasses import dataclass

from src.models.planet import Planet
from src.models.sign import Sign


@dataclass(frozen=True)
class PlanetPosition:
    # -------------------------
    # Identity
    # -------------------------
    planet: Planet

    # -------------------------
    # Astronomy
    # -------------------------
    longitude: float
    latitude: float
    distance: float
    speed: float

    # -------------------------
    # Zodiac (D1)
    # -------------------------
    rashi: Sign
    rashi_number: int
    degrees_in_rashi: float

    # -------------------------
    # Navamsha (D9)
    # -------------------------
    navamsha: Sign
    navamsha_number: int
    navamsha_lord: Planet

    @property
    def is_retrograde(self) -> bool:
        """
        Returns True if the planet is retrograde.
        """
        return self.speed < 0