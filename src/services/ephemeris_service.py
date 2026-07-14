"""
Swiss Ephemeris Service

Responsible for all astronomical calculations.
"""

from datetime import datetime

import swisseph as swe

from models.planet import Planet


class EphemerisService:

    def __init__(self):
        swe.set_ephe_path("data")

    def julian_day(self):

        now = datetime.utcnow()

        return swe.julday(
            now.year,
            now.month,
            now.day,
            now.hour + now.minute / 60.0,
        )

    def current_longitude(self, planet: Planet):

        jd = self.julian_day()

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

        # Ketu is always opposite Rahu
        if planet == Planet.KETU:
            longitude = (longitude + 180.0) % 360.0

        return longitude

    def current_sun_longitude(self):
        return self.current_longitude(Planet.SUN)

    def current_moon_longitude(self):
        return self.current_longitude(Planet.MOON)