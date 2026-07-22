"""
Planet Position Model
"""

from dataclasses import dataclass

from src.models.planet import Planet


@dataclass(frozen=True)
class PlanetPosition:
    """
    Represents the astronomical + astrological position of a planet.
    """

    planet: Planet

    longitude: float
    latitude: float
    distance: float
    speed: float

    # D1
    rashi: str
    rashi_number: int
    degrees_in_rashi: float

    # D9
    navamsha: str
    navamsha_number: int
    navamsha_lord: Planet