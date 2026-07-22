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
    Stateless builder for astronomical charts.
    """

    _ephemeris = EphemerisService()

    @classmethod
    def build(
        cls,
        timestamp: datetime,
        latitude: float,
        longitude: float,
    ) -> Chart:

        ephemeris = cls._ephemeris

        return Chart(
            timestamp=timestamp,
            latitude=latitude,
            longitude=longitude,
            julian_day=ephemeris.julian_day(timestamp),

            sun=ephemeris.get_position(Planet.SUN, timestamp),
            moon=ephemeris.get_position(Planet.MOON, timestamp),
            mercury=ephemeris.get_position(Planet.MERCURY, timestamp),
            venus=ephemeris.get_position(Planet.VENUS, timestamp),
            mars=ephemeris.get_position(Planet.MARS, timestamp),
            jupiter=ephemeris.get_position(Planet.JUPITER, timestamp),
            saturn=ephemeris.get_position(Planet.SATURN, timestamp),
            rahu=ephemeris.get_position(Planet.RAHU, timestamp),
            ketu=ephemeris.get_position(Planet.KETU, timestamp),
        )