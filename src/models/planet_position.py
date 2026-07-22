"""
Planet Position Model
"""

from dataclasses import dataclass

from src.models.planet import Planet


@dataclass(frozen=True)
class PlanetPosition:
    """
    Represents the astronomical position of a planet at a specific timestamp.
    """

    planet: Planet
    longitude: float
    latitude: float
    distance: float
    speed: float