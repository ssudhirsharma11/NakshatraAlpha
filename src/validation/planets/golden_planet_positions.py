"""
Golden Planet Position Dataset

Reference planetary positions validated using Swiss Ephemeris.
"""

from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.planet import Planet


@dataclass(frozen=True)
class ExpectedPlanetPosition:
    longitude: float
    latitude: float
    speed: float


REFERENCE_DATETIME = datetime(
    2026,
    6,
    29,
    9,
    0,
    tzinfo=ZoneInfo("Asia/Kolkata"),
)


GOLDEN_PLANET_POSITIONS = {
    Planet.SUN: ExpectedPlanetPosition(
        longitude=73.20586865,
        latitude=-0.00012047,
        speed=0.95327370,
    ),
    Planet.MOON: ExpectedPlanetPosition(
        longitude=243.88419999,
        latitude=-4.53238951,
        speed=11.88086364,
    ),
    Planet.MARS: ExpectedPlanetPosition(
        longitude=36.00874216,
        latitude=-0.32201152,
        speed=0.71302055,
    ),
    Planet.MERCURY: ExpectedPlanetPosition(
        longitude=92.01466410,
        latitude=-2.01333155,
        speed=0.04519370,
    ),
    Planet.JUPITER: ExpectedPlanetPosition(
        longitude=95.53602790,
        latitude=0.43706631,
        speed=0.21310981,
    ),
    Planet.VENUS: ExpectedPlanetPosition(
        longitude=113.85758010,
        latitude=1.83069402,
        speed=1.13770941,
    ),
    Planet.SATURN: ExpectedPlanetPosition(
        longitude=349.87489236,
        latitude=-2.37426036,
        speed=0.04582844,
    ),
}