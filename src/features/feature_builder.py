"""
Feature Builder

Builds a research-ready FeatureSet from a Chart.
"""

from src.astrology.nakshatra import NakshatraEngine
from src.astrology.tithi import TithiEngine
from src.astrology.planet_relationship import (
    relative_house_distance,
    is_kendra,
)

from src.features.feature_set import FeatureSet

from src.models.chart import Chart
from src.models.planet import Planet


class FeatureBuilder:
    """
    Converts a Chart into a research FeatureSet.
    """

    @staticmethod
    def build(chart: Chart) -> FeatureSet:

        # ----------------------------------------
        # Nakshatra Features
        # ----------------------------------------

        moon_nak = NakshatraEngine.calculate(
            chart,
            Planet.MOON,
        )

        sun_nak = NakshatraEngine.calculate(
            chart,
            Planet.SUN,
        )

        # ----------------------------------------
        # Tithi Features
        # ----------------------------------------

        tithi = TithiEngine.calculate(chart)

        # ----------------------------------------
        # Planet Relationship Features
        # ----------------------------------------

        saturn_distance = relative_house_distance(
            chart.sun,
            chart.saturn,
        )

        # ----------------------------------------
        # Build Feature Set
        # ----------------------------------------

        return FeatureSet(

            chart=chart,

            # --------------------------
            # Nakshatra
            # --------------------------

            moon_nakshatra=moon_nak.nakshatra.name,
            moon_nakshatra_number=moon_nak.number,

            sun_nakshatra=sun_nak.nakshatra.name,
            sun_nakshatra_number=sun_nak.number,

            # --------------------------
            # Tithi
            # --------------------------

            tithi=tithi.tithi.name,
            tithi_number=tithi.number,

            paksha=tithi.paksha,

            # --------------------------
            # Planet Relationships
            # --------------------------

            saturn_from_sun=saturn_distance,

            saturn_kendra_from_sun=is_kendra(
                saturn_distance
            ),
        )