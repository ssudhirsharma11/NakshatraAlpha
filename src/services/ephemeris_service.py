"""
Swiss Ephemeris Service

Responsible for all astronomical calculations.
"""

from datetime import datetime, timezone

import swisseph as swe

from src.astrology.navamsha import navamsha_details
from src.models.planet import Planet
from src.models.planet_position import PlanetPosition


class EphemerisService:
    """
    Provides deterministic planetary positions using Swiss Ephemeris.
    """

    def __init__(self):
        swe.set_ephe_path("data")
        swe.set_sid_mode(swe.SIDM_LAHIRI)

    @staticmethod
    def julian_day(timestamp: datetime) -> float:
        """
        Convert a timezone-aware datetime into Julian Day (UTC).
        """

        utc_time = timestamp.astimezone(timezone.utc)

        hour = (
            utc_time.hour
            + utc_time.minute / 60.0
            + utc_time.second / 3600.0
            + utc_time.microsecond / 3_600_000_000.0
        )

        return swe.julday(
            utc_time.year,
            utc_time.month,
            utc_time.day,
            hour,
        )

    @staticmethod
    def _planet_map():
        return {
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

    def get_position(
        self,
        planet: Planet,
        timestamp: datetime,
    ) -> PlanetPosition:

        jd = self.julian_day(timestamp)

        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

        result, _ = swe.calc_ut(
            jd,
            self._planet_map()[planet],
            flags,
        )

        longitude = result[0]
        latitude = result[1]
        distance = result[2]
        speed = result[3]

        if planet == Planet.KETU:
            longitude = (longitude + 180.0) % 360.0

        # -----------------------------
        # Astrology Calculations (D1/D9)
        # -----------------------------
        details = navamsha_details(longitude)

        return PlanetPosition(
            planet=planet,

            longitude=longitude,
            latitude=latitude,
            distance=distance,
            speed=speed,

            rashi=details["rashi"],
            rashi_number=details["rashi_number"],
            degrees_in_rashi=details["degrees_in_rashi"],

            navamsha=details["navamsha"],
            navamsha_number=details["navamsha_number"],
            navamsha_lord=details["navamsha_lord"],
        )

    def get_longitude(
        self,
        planet: Planet,
        timestamp: datetime,
    ) -> float:
        """
        Backward-compatible wrapper.
        """

        return self.get_position(
            planet,
            timestamp,
        ).longitude