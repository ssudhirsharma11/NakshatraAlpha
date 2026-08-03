"""
Report Builder

Builds research reports directly from the production pipeline.

This class never reads research_dataset.csv.
Everything is rebuilt live from:

ChartBuilder
HoraService
FeatureBuilder
HoraMarketService
MarketFeatureBuilder
"""

from __future__ import annotations

from datetime import date, datetime

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


class ReportBuilder:
    """
    Builds research reports using the live production pipeline.
    """

    def __init__(self):

        self.hora_service = HoraService()

        self.feature_builder = FeatureBuilder()

        self.market_service = HoraMarketService()

    # ==========================================================
    # PUBLIC METHODS
    # ==========================================================

    def build_timestamp(
        self,
        timestamp: datetime,
    ) -> HoraReport:
        """
        Build report for one timestamp.

        The active Hora is automatically determined.
        """

        hora = self.hora_service.get_hora(
            timestamp=timestamp,
            location=RESEARCH_LOCATION,
        )

        return self._build_hora_report(
            hora
        )

    def build_day(
        self,
        report_date: date,
    ) -> ResearchReport:
        def build_day(
    self,
    report_date: date,
) -> ResearchReport:
    """
    Build report for every daytime Hora.
    """

    horas = self.hora_service.get_day_horas(
        calculation_date=report_date,
        location=RESEARCH_LOCATION,
    )

    report = ResearchReport()

    for hora in horas:

        try:

            report.horas.append(
                self._build_hora_report(hora)
            )

        except Exception as ex:

            print(
                f"Skipped {hora.start} : {ex}"
            )

    return report
        raise NotImplementedError

    def build_range(
        self,
        start_date: date,
        end_date: date,
    ) -> ResearchReport:
        """
        Placeholder.

        Part 2B will implement this.
        """

        raise NotImplementedError

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

    def _build_hora_report(
        self,
        hora,
    ) -> HoraReport:
        """
        Build complete report for one Hora.

        Astrology and market sections are
        implemented in Part 2B / Part 2C.
        """

        chart = self._build_chart(
            hora.start
        )

        features = self.feature_builder.build(
            chart
        )

        market = self.market_service.build(
            hora
        )

        # ------------------------------------------------------
        # Placeholders
        # ------------------------------------------------------

        astrology = AstrologySection()

        planets = PlanetSection()

        market_section = MarketSection()

        # ------------------------------------------------------

        return HoraReport(
            date=str(hora.start.date()),
            hora_start=str(hora.start),
            hora_end=str(hora.end),
            astrology=astrology,
            planets=planets,
            market=market_section,
        )
    