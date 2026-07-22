"""
Tithi Engine

Calculates the current Tithi from the angular distance
between the Sun and Moon.
"""

from src.knowledge.tithi_data import (
    TITHI_DATA,
    TITHI_SIZE,
)
from src.models.chart import Chart
from src.models.planet import Planet
from src.models.tithi_enum import Tithi
from src.models.tithi_position import TithiPosition


class TithiEngine:
    """
    Calculates the current Tithi.
    """

    @staticmethod
    def calculate(chart: Chart) -> TithiPosition:
        """
        Calculate the lunar tithi for the supplied chart.
        """

        sun_longitude = chart.get(Planet.SUN).longitude % 360.0
        moon_longitude = chart.get(Planet.MOON).longitude % 360.0

        angular_distance = (moon_longitude - sun_longitude) % 360.0

        index = int(angular_distance / TITHI_SIZE)

        tithi = list(Tithi)[index]

        metadata = TITHI_DATA[tithi]

        degrees_in_tithi = angular_distance - metadata.start_angle

        degrees_remaining = metadata.end_angle - angular_distance

        return TithiPosition(
            tithi=metadata.tithi,
            number=metadata.number,
            paksha=metadata.paksha,
            angular_distance=angular_distance,
            degrees_in_tithi=degrees_in_tithi,
            degrees_remaining=degrees_remaining,
        )