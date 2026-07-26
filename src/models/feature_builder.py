"""
Feature Builder

Converts a Chart into a FeatureSet.
"""

from src.astrology.planet_relationship import (
    relative_house_distance,
    is_kendra,
)

from src.models.feature_set import FeatureSet
from src.astrology.zodiac import ZodiacEngine


class FeatureBuilder:
    """
    Builds derived research features from
    an astronomical chart.
    """

    def build(self, chart):
        """
        Generate all research features.
        """

        saturn_distance = relative_house_distance(
            chart.sun,
            chart.saturn,
        )

        sun_sign = ZodiacEngine.sign(chart.sun.longitude)
        moon_sign = ZodiacEngine.sign(chart.moon.longitude)
        saturn_sign = ZodiacEngine.sign(chart.saturn.longitude)

        return FeatureSet(
            chart=chart,

            # Calendar
            weekday=chart.datetime.weekday(),

            # Planet positions
            sun_longitude=chart.sun.longitude,
            moon_longitude=chart.moon.longitude,

            sun_sign=sun_sign,
            sun_sign_number=sun_sign.number,

            moon_sign=moon_sign,
            moon_sign_number=moon_sign.number,

            saturn_sign=saturn_sign,

            # Relationships
            saturn_from_sun=saturn_distance,

            saturn_kendra_from_sun=is_kendra(
                saturn_distance
            ),
        )