"""
Swiss Ephemeris Service

Provides astronomical calculations using Swiss Ephemeris.
"""

from datetime import datetime
import swisseph as swe


class EphemerisService:

    def __init__(self):
        # Path for ephemeris files (we'll download them later)
        swe.set_ephe_path("data/ephemeris")

    def current_sun_longitude(self):

        now = datetime.utcnow()

        julian_day = swe.julday(
            now.year,
            now.month,
            now.day,
            now.hour + now.minute / 60.0
        )

        result, _ = swe.calc_ut(julian_day, swe.SUN)

        return result[0]