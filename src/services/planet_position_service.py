"""
Planet Position Service

Returns sidereal planetary positions for all supported planets.

This service delegates the actual planetary calculations to
EphemerisService so there is a single source of truth for creating
PlanetPosition objects.
"""

from datetime import datetime

from src.models.location import Location
from src.models.planet import Planet
from src.models.planet_position import PlanetPosition
from src.services.ephemeris_service import EphemerisService


class PlanetPositionService:
    """
    Service returning planetary positions for an entire chart.
    """

    def __init__(self):
        self._ephemeris = EphemerisService()

    def get_positions(
        self,
        calculation_datetime: datetime,
        location: Location,
    ) -> dict[Planet, PlanetPosition]:

        # Reserved for future use (e.g. topocentric calculations)
        _ = location

        positions: dict[Planet, PlanetPosition] = {}

        for planet in (
            Planet.SUN,
            Planet.MOON,
            Planet.MERCURY,
            Planet.VENUS,
            Planet.MARS,
            Planet.JUPITER,
            Planet.SATURN,
            Planet.RAHU,
            Planet.KETU,
        ):
            positions[planet] = self._ephemeris.get_position(
                planet,
                calculation_datetime,
            )

        return positions