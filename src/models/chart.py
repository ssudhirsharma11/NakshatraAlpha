"""
Chart Model

Represents one astronomical snapshot.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class PlanetPosition:
    name: str
    longitude: float
    latitude: float
    distance: float
    speed: float


@dataclass
class Chart:

    timestamp: datetime

    latitude: float
    longitude: float

    julian_day: float

    sun: PlanetPosition
    moon: PlanetPosition
    mars: PlanetPosition
    mercury: PlanetPosition
    jupiter: PlanetPosition
    venus: PlanetPosition
    saturn: PlanetPosition
    rahu: PlanetPosition
    ketu: PlanetPosition