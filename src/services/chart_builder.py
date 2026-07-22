"""
Chart Builder

Builds a complete astronomical chart.
"""

from datetime import datetime

from src.models.chart import Chart
from src.models.planet import Planet
from src.services.ephemeris_service import EphemerisService


class ChartBuilder:
    """
    Builds a complete Chart for a given timestamp and location.
    """

    def __init__(self):
        self.ephemeris = EphemerisService()

    def build(
        self,
        timestamp: datetime,
        latitude: float,
        longitude: float,
    ) -> Chart:

        return Chart(
            timestamp=timestamp,
            latitude=latitude,
            longitude=longitude,
            julian_day=self.ephemeris.julian_day(timestamp),

            sun=self.ephemeris.get_position(Planet.SUN, timestamp),
            moon=self.ephemeris.get_position(Planet.MOON, timestamp),
            mercury=self.ephemeris.get_position(Planet.MERCURY, timestamp),
            venus=self.ephemeris.get_position(Planet.VENUS, timestamp),
            mars=self.ephemeris.get_position(Planet.MARS, timestamp),
            jupiter=self.ephemeris.get_position(Planet.JUPITER, timestamp),
            saturn=self.ephemeris.get_position(Planet.SATURN, timestamp),
            rahu=self.ephemeris.get_position(Planet.RAHU, timestamp),
            ketu=self.ephemeris.get_position(Planet.KETU, timestamp),
        )