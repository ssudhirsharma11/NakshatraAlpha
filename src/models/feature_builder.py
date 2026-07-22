"""
Feature Builder

Converts a Chart into a FeatureSet.
"""

from src.astrology.planet_relationship import (
    relative_house_distance,
    is_kendra,
)

from src.models.chart import Chart
from src.models.feature_set import FeatureSet


class FeatureBuilder:
    """
    Builds derived research features from
    an astronomical chart.
    """

    def build(self, chart: Chart) -> FeatureSet:
        """
        Generate all research features.
        """

        saturn_distance = relative_house_distance(
            chart.sun,
            chart.saturn,
        )

        return FeatureSet(
            chart=chart,

            saturn_from_sun=saturn_distance,

            saturn_kendra_from_sun=is_kendra(
                saturn_distance
            ),
        )