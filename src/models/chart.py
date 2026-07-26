"""
Chart Model

Represents one astronomical snapshot.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from src.models.planet import Planet
from src.models.planet_position import PlanetPosition

if TYPE_CHECKING:
    from src.models.lagna_position import LagnaPosition


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

    # Astrology modules populate this as they become available.
    # None indicates the value has not yet been calculated.
    lagna: LagnaPosition | None = None

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