"""
Feature Builder

Converts a Chart into a FeatureSet.
"""

from src.astrology.planet_relationship import (
    is_kendra,
    relative_house_distance,
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

            # ------------------------------------------------------------------
            # Calendar
            # ------------------------------------------------------------------

            weekday=chart.timestamp.weekday(),

            # ------------------------------------------------------------------
            # Planet Positions
            # ------------------------------------------------------------------

            sun_longitude=chart.sun.longitude,
            moon_longitude=chart.moon.longitude,

            sun_sign=chart.sun.rashi,
            sun_sign_number=chart.sun.rashi_number,

            moon_sign=chart.moon.rashi,
            moon_sign_number=chart.moon.rashi_number,

            sun_navamsha=chart.sun.navamsha,
            moon_navamsha=chart.moon.navamsha,

            saturn_sign=chart.saturn.rashi,

            # ------------------------------------------------------------------
            # Relationships
            # ------------------------------------------------------------------

            saturn_from_sun=saturn_distance,
            saturn_kendra_from_sun=is_kendra(
                saturn_distance
            ),
        )