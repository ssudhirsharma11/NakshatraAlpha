"""
Feature Builder

Converts a Chart into a FeatureSet.
"""

from src.astrology.nakshatra import NakshatraEngine
from src.astrology.planet_relationship import (
    is_kendra,
    relative_house_distance,
)
from src.astrology.sade_sati import SadeSatiEngine
from src.astrology.tithi import TithiEngine
from src.models.chart import Chart
from src.models.feature_set import FeatureSet
from src.models.planet import Planet


class FeatureBuilder:
    """
    Builds all derived astrological research features
    from a Chart.
    """

    def build(
        self,
        chart: Chart,
    ) -> FeatureSet:

        # -----------------------------------------------------
        # Planet Relationships
        # -----------------------------------------------------

        saturn_from_sun = relative_house_distance(
            chart.sun,
            chart.saturn,
        )

        saturn_from_moon = relative_house_distance(
            chart.moon,
            chart.saturn,
        )

        saturn_kendra_from_sun = is_kendra(
            saturn_from_sun,
        )

        saturn_kendra_from_moon = is_kendra(
            saturn_from_moon,
        )

        # -----------------------------------------------------
        # Sade Sati
        # -----------------------------------------------------

        sade_sati = SadeSatiEngine.calculate(
            saturn_from_moon,
        )

        # -----------------------------------------------------
        # Nakshatra
        # -----------------------------------------------------

        moon_nakshatra = NakshatraEngine.calculate(
            chart,
            Planet.MOON,
        )

        sun_nakshatra = NakshatraEngine.calculate(
            chart,
            Planet.SUN,
        )

        # -----------------------------------------------------
        # Tithi
        # -----------------------------------------------------

        tithi = TithiEngine.calculate(
            chart,
        )

        # -----------------------------------------------------
        # Feature Set
        # -----------------------------------------------------

        return FeatureSet(

            # -------------------------------------------------
            # Source
            # -------------------------------------------------

            chart=chart,

            # -------------------------------------------------
            # Calendar
            # -------------------------------------------------

            weekday=chart.timestamp.weekday(),

            # -------------------------------------------------
            # Tithi
            # -------------------------------------------------

            tithi=tithi.tithi,
            tithi_number=tithi.number,
            paksha=tithi.paksha,

            tithi_group=tithi.tithi_group,
            tithi_lord=tithi.tithi_lord,

            # -------------------------------------------------
            # Nakshatra
            # -------------------------------------------------

            moon_nakshatra=moon_nakshatra.nakshatra,
            moon_nakshatra_number=moon_nakshatra.number,

            sun_nakshatra=sun_nakshatra.nakshatra,
            sun_nakshatra_number=sun_nakshatra.number,

            pada=moon_nakshatra.pada,

            # -------------------------------------------------
            # Lagna
            # -------------------------------------------------

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

            # Degrees within the sign (matches JHora)
            lagna_degree=(
                chart.lagna.degrees_in_rashi
                if chart.lagna
                else None
            ),

            # -------------------------------------------------
            # Planet Positions
            # -------------------------------------------------

            sun_longitude=chart.sun.longitude,
            moon_longitude=chart.moon.longitude,

            sun_sign=chart.sun.rashi,
            sun_sign_number=chart.sun.rashi_number,

            moon_sign=chart.moon.rashi,
            moon_sign_number=chart.moon.rashi_number,

            sun_navamsha=chart.sun.navamsha,
            moon_navamsha=chart.moon.navamsha,

            saturn_sign=chart.saturn.rashi,

            # -------------------------------------------------
            # Relationships
            # -------------------------------------------------

            saturn_from_sun=saturn_from_sun,
            saturn_kendra_from_sun=saturn_kendra_from_sun,

            saturn_from_moon=saturn_from_moon,
            saturn_kendra_from_moon=saturn_kendra_from_moon,

            # -------------------------------------------------
            # Sade Sati
            # -------------------------------------------------

            sade_sati=sade_sati.active,
            sade_sati_phase=sade_sati.phase,
        )