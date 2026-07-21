"""
Swiss Ephemeris Service

Responsible for all astronomical calculations.
"""

from datetime import datetime

import swisseph as swe

from src.models.planet import Planet


class EphemerisService:

    def __init__(self):
        swe.set_ephe_path("data")

    @staticmethod
    def julian_day(timestamp: datetime) -> float:
        """
        Convert a datetime into Julian Day (UTC).
        """

        utc_time = timestamp.astimezone().astimezone()

        hour = (
            utc_time.hour
            + utc_time.minute / 60.0
            + utc_time.second / 3600.0
        )

        return swe.julday(
            utc_time.year,
            utc_time.month,
            utc_time.day,
            hour,
        )

    def get_longitude(
        self,
        planet: Planet,
        timestamp: datetime,
    ) -> float:

        jd = self.julian_day(timestamp)

        planet_map = {
            Planet.SUN: swe.SUN,
            Planet.MOON: swe.MOON,
            Planet.MERCURY: swe.MERCURY,
            Planet.VENUS: swe.VENUS,
            Planet.MARS: swe.MARS,
            Planet.JUPITER: swe.JUPITER,
            Planet.SATURN: swe.SATURN,
            Planet.RAHU: swe.MEAN_NODE,
            Planet.KETU: swe.MEAN_NODE,
        }

        result, _ = swe.calc_ut(
            jd,
            planet_map[planet],
        )

        longitude = result[0]

        if planet == Planet.KETU:
            longitude = (longitude + 180.0) % 360.0

        return round(longitude, 6)