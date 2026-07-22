"""
Feature Builder

Builds a research-ready FeatureSet from a Chart.
"""

from src.astrology.nakshatra import NakshatraEngine
from src.astrology.tithi import TithiEngine

from src.features.feature_set import FeatureSet

from src.models.chart import Chart
from src.models.planet import Planet


class FeatureBuilder:
    """
    Converts a Chart into a research FeatureSet.
    """

    @staticmethod
    def build(chart: Chart) -> FeatureSet:

        moon_nak = NakshatraEngine.calculate(
            chart,
            Planet.MOON,
        )

        sun_nak = NakshatraEngine.calculate(
            chart,
            Planet.SUN,
        )

        tithi = TithiEngine.calculate(chart)

        return FeatureSet(
            moon_nakshatra=moon_nak.nakshatra.name,
            moon_nakshatra_number=moon_nak.number,

            sun_nakshatra=sun_nak.nakshatra.name,
            sun_nakshatra_number=sun_nak.number,

            tithi=tithi.tithi.name,
            tithi_number=tithi.number,

            paksha=tithi.paksha,
        )