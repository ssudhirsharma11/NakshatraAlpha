"""
Planet Position Model
"""

from dataclasses import dataclass

from models.planet import Planet


@dataclass
class PlanetPosition:

    planet: Planet
    longitude: float
    latitude: float
    speed: float