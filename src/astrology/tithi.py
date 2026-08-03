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
        Calculate the lunar Tithi for the supplied chart.
        """

        sun_longitude = (
            chart.get(Planet.SUN).longitude % 360.0
        )

        moon_longitude = (
            chart.get(Planet.MOON).longitude % 360.0
        )

        angular_distance = (
            moon_longitude - sun_longitude
        ) % 360.0

        index = int(
            angular_distance / TITHI_SIZE
        )

        tithi = Tithi(index + 1)

        metadata = TITHI_DATA[tithi]

        degrees_in_tithi = (
            angular_distance
            - metadata.start_angle
        )

        degrees_remaining = (
            TITHI_SIZE
            - degrees_in_tithi
        )

        progress = (
            degrees_in_tithi
            / TITHI_SIZE
        ) * 100.0

        return TithiPosition(

            # -------------------------------------------------
            # Basic Information
            # -------------------------------------------------

            tithi=metadata.tithi,

            number=metadata.number,

            paksha=metadata.paksha,

            # -------------------------------------------------
            # Research Classification
            # -------------------------------------------------

            tithi_group=metadata.tithi_group,

            tithi_lord=metadata.tithi_lord,

            # -------------------------------------------------
            # Astronomy
            # -------------------------------------------------

            angular_distance=angular_distance,

            degrees_in_tithi=degrees_in_tithi,

            degrees_remaining=degrees_remaining,

            progress=progress,
        )