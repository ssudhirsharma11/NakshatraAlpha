"""
Chart Model

Represents one astronomical snapshot.
"""

from dataclasses import dataclass
from datetime import datetime

from src.models.planet import Planet
from src.models.planet_position import PlanetPosition


@dataclass(frozen=True)
class Chart:
    """
    Represents a complete astronomical snapshot
    for a given timestamp and location.
    """

    timestamp: datetime

    latitude: float
    longitude: float

    julian_day: float

    sun: PlanetPosition
    moon: PlanetPosition
    mercury: PlanetPosition
    venus: PlanetPosition
    mars: PlanetPosition
    jupiter: PlanetPosition
    saturn: PlanetPosition
    rahu: PlanetPosition
    ketu: PlanetPosition

    def get(self, planet: Planet) -> PlanetPosition:
        """
        Returns the position of the requested planet.
        """
        return self.all_positions()[planet]

    def all_positions(self) -> dict[Planet, PlanetPosition]:
        """
        Returns all planetary positions as a dictionary.
        """

        return {
            Planet.SUN: self.sun,
            Planet.MOON: self.moon,
            Planet.MERCURY: self.mercury,
            Planet.VENUS: self.venus,
            Planet.MARS: self.mars,
            Planet.JUPITER: self.jupiter,
            Planet.SATURN: self.saturn,
            Planet.RAHU: self.rahu,
            Planet.KETU: self.ketu,
        }