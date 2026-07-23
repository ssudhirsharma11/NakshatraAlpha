"""
Planet Position Service

Calculates sidereal planetary positions using Swiss Ephemeris.
"""

from datetime import datetime, timezone

import swisseph as swe

from src.models.location import Location
from src.models.planet import Planet
from src.models.planet_position import PlanetPosition


PLANET_MAPPING = {
    Planet.SUN: swe.SUN,
    Planet.MOON: swe.MOON,
    Planet.MARS: swe.MARS,
    Planet.MERCURY: swe.MERCURY,
    Planet.JUPITER: swe.JUPITER,
    Planet.VENUS: swe.VENUS,
    Planet.SATURN: swe.SATURN,
}


class PlanetPositionService:

    def __init__(self):

        swe.set_sid_mode(swe.SIDM_LAHIRI)

    def get_positions(
        self,
        calculation_datetime: datetime,
        location: Location,
    ) -> dict[Planet, PlanetPosition]:

        # Convert local time to UTC
        utc_dt = calculation_datetime.astimezone(timezone.utc)

        jd = swe.julday(
            utc_dt.year,
            utc_dt.month,
            utc_dt.day,
            utc_dt.hour
            + utc_dt.minute / 60
            + utc_dt.second / 3600,
        )

        flags = (
        swe.FLG_SWIEPH
        | swe.FLG_SIDEREAL
        | swe.FLG_SPEED
)

        positions = {}

        for planet, swe_planet in PLANET_MAPPING.items():

            result, _ = swe.calc_ut(
                jd,
                swe_planet,
                flags,
            )

            positions[planet] = PlanetPosition(
                planet=planet,
                longitude=result[0] % 360,
                latitude=result[1],
                speed=result[3],
            )

        return positions