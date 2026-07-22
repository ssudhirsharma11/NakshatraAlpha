"""
Nakshatra Engine

Calculates the Nakshatra occupied by a planet.
"""

from src.knowledge.nakshatra_data import (
    NAKSHATRA_DATA,
    NAKSHATRA_SIZE,
    PADA_SIZE,
)
from src.models.chart import Chart
from src.models.nakshatra_enum import Nakshatra
from src.models.nakshatra_position import NakshatraPosition
from src.models.planet import Planet


class NakshatraEngine:
    """
    Calculates Nakshatra information for a planet.
    """

    @staticmethod
    def calculate(
        chart: Chart,
        planet: Planet,
    ) -> NakshatraPosition:

        longitude = chart.get(planet).longitude % 360.0

        index = int(longitude / NAKSHATRA_SIZE)

        nakshatra = list(Nakshatra)[index]

        metadata = NAKSHATRA_DATA[nakshatra]

        degrees_in = longitude - metadata.start_degree

        degrees_remaining = metadata.end_degree - longitude

        pada = int(degrees_in / PADA_SIZE) + 1

        # Safety against floating point edge cases
        pada = max(1, min(4, pada))

        return NakshatraPosition(
            planet=planet,
            nakshatra=metadata.nakshatra,
            number=metadata.number,
            pada=pada,
            lord=metadata.lord,
            degrees_in_nakshatra=degrees_in,
            degrees_remaining=degrees_remaining,
        )