"""
Feature Builder

Converts a Chart into a FeatureSet.
"""

from src.astrology.nakshatra import NakshatraEngine
from src.astrology.planet_relationship import (
    is_kendra,
    relative_house_distance,
)
from src.astrology.tithi import TithiEngine
from src.models.chart import Chart
from src.models.feature_set import FeatureSet
from src.models.planet import Planet


class FeatureBuilder:
    """
    Builds derived research features from
    an astronomical chart.
    """

    def build(
        self,
        chart: Chart,
    ) -> FeatureSet:
        """
        Generate all research features.
        """

        saturn_distance = relative_house_distance(
            chart.sun,
            chart.saturn,
        )

        moon_nakshatra = NakshatraEngine.calculate(
            chart,
            Planet.MOON,
        )

        sun_nakshatra = NakshatraEngine.calculate(
            chart,
            Planet.SUN,
        )

        tithi = TithiEngine.calculate(chart)

        return FeatureSet(
            chart=chart,

            # ------------------------------------------------------------------
            # Calendar
            # ------------------------------------------------------------------

            weekday=chart.timestamp.weekday(),

            # ------------------------------------------------------------------
            # Tithi
            # ------------------------------------------------------------------

            tithi=tithi.tithi,
            tithi_number=tithi.number,
            paksha=tithi.paksha,

            # ------------------------------------------------------------------
            # Nakshatra
            # ------------------------------------------------------------------

            moon_nakshatra=moon_nakshatra.nakshatra,
            moon_nakshatra_number=moon_nakshatra.number,

            sun_nakshatra=sun_nakshatra.nakshatra,
            sun_nakshatra_number=sun_nakshatra.number,

            pada=moon_nakshatra.pada,

            # ------------------------------------------------------------------
            # Lagna
            # ------------------------------------------------------------------

            lagna_sign=(
                chart.lagna.rashi
                if chart.lagna
                else None
            ),

            lagna_number=(
                chart.lagna.rashi_number
                if chart.lagna
                else None
            ),

            lagna_degree=(
                chart.lagna.longitude
                if chart.lagna
                else None
            ),

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