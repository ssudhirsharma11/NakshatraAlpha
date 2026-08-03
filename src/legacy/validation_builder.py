"""
Validation Builder

Builds validation reports directly from the
production pipeline.

This class NEVER reads research_dataset.csv.

Everything is rebuilt live using:

- HoraService
- ChartBuilder
- FeatureBuilder
- HoraMarketService
- MarketFeatureBuilder
"""

from __future__ import annotations

from datetime import date, datetime, timedelta

from src.config.research_config import RESEARCH_LOCATION
from src.features.feature_builder import FeatureBuilder
from src.features.market_feature_builder import MarketFeatureBuilder
from src.research.report_models import (
    AstrologySection,
    HoraReport,
    MarketSection,
    PlanetSection,
    ResearchReport,
)
from src.services.chart_builder import ChartBuilder
from src.services.hora_market_service import HoraMarketService
from src.services.hora_service import HoraService


class ValidationBuilder:
    """
    Builds validation reports from the
    live production pipeline.
    """

    def __init__(self):

        self.hora_service = HoraService()

        self.feature_builder = FeatureBuilder()

        self.market_service = HoraMarketService()

    # ==========================================================
    # PUBLIC
    # ==========================================================

    def build_timestamp(
        self,
        timestamp: datetime,
    ) -> ResearchReport:

        hora = self.hora_service.get_hora(
            timestamp=timestamp,
            location=RESEARCH_LOCATION,
        )

        report = ResearchReport()

        report.horas.append(
            self._build_hora(hora)
        )

        return report

    def build_day(
        self,
        report_date: date,
        hora_filter: int | None = None,
    ) -> ResearchReport:

        horas = self.hora_service.get_day_horas(
            calculation_date=report_date,
            location=RESEARCH_LOCATION,
        )

        report = ResearchReport()

        for hora in horas:

            if (
                hora_filter is not None
                and hora.index != hora_filter
            ):
                continue

            try:

                report.horas.append(
                    self._build_hora(hora)
                )

            except Exception as ex:

                print(
                    f"Skipped {hora.start} : {ex}"
                )

        return report

    def build_range(
        self,
        start_date: date,
        end_date: date,
        hora_filter: int | None = None,
    ) -> ResearchReport:

        report = ResearchReport()

        current = start_date

        while current <= end_date:

            daily = self.build_day(
                current,
                hora_filter,
            )

            report.horas.extend(
                daily.horas
            )

            current += timedelta(days=1)

        return report

    # ==========================================================
    # INTERNAL
    # ==========================================================

    def _build_chart(
        self,
        timestamp: datetime,
    ):

        return ChartBuilder.build(
            timestamp=timestamp,
            latitude=RESEARCH_LOCATION.latitude,
            longitude=RESEARCH_LOCATION.longitude,
        )

    def _build_hora(
        self,
        hora,
    ) -> HoraReport:

        chart = self._build_chart(
            hora.start
        )

        features = self.feature_builder.build(
            chart
        )

        market_result = self.market_service.build(
            hora
        )

        market_features = MarketFeatureBuilder.build(
            open_price=market_result.market.open,
            high_price=market_result.market.high,
            low_price=market_result.market.low,
            close_price=market_result.market.close,
        )

        astrology = self._build_astrology(
            hora,
            features,
        )

        planets = self._build_planets(
            chart
        )

        market = self._build_market(
            market_result.market,
            market_features,
        )

        return HoraReport(
            date=str(hora.start.date()),
            hora_start=str(hora.start),
            hora_end=str(hora.end),
            astrology=astrology,
            planets=planets,
            market=market,
        )    def _build_astrology(
        self,
        hora,
        features,
    ) -> AstrologySection:
        """
        Build astrology section.
        """

        return AstrologySection(

            weekday=hora.start.strftime("%A"),

            hora_number=hora.index,

            hora_lord=hora.planet.name,

            tithi=(
                features.tithi.name
                if features.tithi
                else ""
            ),

            # Will be populated once
            # TithiEngine exposes the lord.
            tithi_lord="",

            paksha=(
                features.paksha.name
                if features.paksha
                else ""
            ),

            moon_nakshatra=(
                features.moon_nakshatra.name
                if features.moon_nakshatra
                else ""
            ),

            moon_pada=(
                features.pada
                if features.pada
                else 0
            ),

            moon_sign=(
                features.moon_sign.name
                if features.moon_sign
                else ""
            ),

            moon_navamsha=(
                features.moon_navamsha.name
                if features.moon_navamsha
                else ""
            ),

            sun_sign=(
                features.sun_sign.name
                if features.sun_sign
                else ""
            ),

            sun_navamsha=(
                features.sun_navamsha.name
                if features.sun_navamsha
                else ""
            ),

            lagna=(
                features.lagna_sign.name
                if features.lagna_sign
                else ""
            ),

            lagna_degree=(
                round(
                    features.lagna_degree,
                    2,
                )
                if features.lagna_degree is not None
                else 0.0
            ),

            saturn_sign=(
                features.saturn_sign.name
                if features.saturn_sign
                else ""
            ),

            saturn_from_sun=(
                features.saturn_from_sun
                if features.saturn_from_sun is not None
                else 0
            ),

            saturn_from_moon=(
                features.saturn_from_moon
                if features.saturn_from_moon is not None
                else 0
            ),

            saturn_kendra=bool(
                features.saturn_kendra_from_sun
            ),

            sade_sati=bool(
                features.sade_sati
            ),

            sade_sati_phase=(
                features.sade_sati_phase
                if features.sade_sati_phase
                else ""
            ),
        )

    def _build_planets(
        self,
        chart,
    ) -> PlanetSection:
        """
        Build planetary longitude section.
        """

        return PlanetSection(

            sun=round(
                chart.sun.longitude,
                4,
            ),

            moon=round(
                chart.moon.longitude,
                4,
            ),

            mars=round(
                chart.mars.longitude,
                4,
            ),

            mercury=round(
                chart.mercury.longitude,
                4,
            ),

            jupiter=round(
                chart.jupiter.longitude,
                4,
            ),

            venus=round(
                chart.venus.longitude,
                4,
            ),

            saturn=round(
                chart.saturn.longitude,
                4,
            ),

            rahu=round(
                chart.rahu.longitude,
                4,
            ),

            ketu=round(
                chart.ketu.longitude,
                4,
            ),
        )