"""
Planet Position Model

Represents the astronomical position of a planet.
"""

from dataclasses import dataclass

from src.models.planet import Planet


@dataclass(frozen=True)
class PlanetPosition:
    planet: Planet

    # Sidereal longitude (0°–360°)
    longitude: float

    # Ecliptic latitude
    latitude: float

    # Daily motion (degrees/day)
    speed: float

    @property
    def is_retrograde(self) -> bool:
        return self.speed < 0