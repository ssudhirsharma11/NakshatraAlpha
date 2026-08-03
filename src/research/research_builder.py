"""
Research Builder

Builds research rows for

- Timestamp
- Trading Day
- Date Range
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta

from src.config.research_config import RESEARCH_LOCATION
from src.features.feature_builder import FeatureBuilder
from src.features.market_feature_builder import (
    MarketFeatureBuilder,
)
from src.models.research_report_row import (
    ResearchReportRow,
)
from src.services.chart_builder import ChartBuilder
from src.services.hora_market_service import (
    HoraMarketService,
)
from src.services.hora_service import HoraService


class ResearchBuilder:
    """
    Builds research report rows.
    """

    MARKET_OPEN = time(
        9,
        15,
    )

    MARKET_CLOSE = time(
        15,
        30,
    )

    def __init__(self):

        self.hora_service = HoraService()

        self.feature_builder = FeatureBuilder()

        self.market_service = HoraMarketService()

    # ---------------------------------------------------------

    def build_timestamp(
        self,
        timestamp: datetime,
    ) -> list[ResearchReportRow]:

        return self.build_day(
            timestamp.date(),
        )

    # ---------------------------------------------------------

    def build_day(
        self,
        report_date: date,
        hora_number: int | None = None,
    ) -> list[ResearchReportRow]:

        rows: list[
            ResearchReportRow
        ] = []

        horas = self.hora_service.get_day_horas(
            report_date,
            RESEARCH_LOCATION,
        )

        market_open = datetime.combine(
            report_date,
            self.MARKET_OPEN,
            tzinfo=horas[0].start.tzinfo,
        )

        market_close = datetime.combine(
            report_date,
            self.MARKET_CLOSE,
            tzinfo=horas[0].start.tzinfo,
        )

        for hora in horas:

            if (
                hora_number is not None
                and hora.index != hora_number
            ):
                continue

            overlap_start = max(
                hora.start,
                market_open,
            )

            overlap_end = min(
                hora.end,
                market_close,
            )

            if overlap_start >= overlap_end:
                continue

            rows.append(

                self._build_row(

                    hora=hora,

                    market_start=overlap_start,

                    market_end=overlap_end,
                )

            )

        return rows

    # ---------------------------------------------------------

    def build_range(
        self,
        start_date: date,
        end_date: date,
        hora_number: int | None = None,
    ) -> list[ResearchReportRow]:

        rows: list[
            ResearchReportRow
        ] = []

        current = start_date

        while current <= end_date:

            rows.extend(

                self.build_day(
                    current,
                    hora_number,
                )

            )

            current += timedelta(
                days=1,
            )

        return rows    # ---------------------------------------------------------

    def _build_row(
        self,
        hora,
        market_start,
        market_end,
    ) -> ResearchReportRow:
        """
        Builds one research report row.
        """

        # -----------------------------------------------------
        # Astrology
        # -----------------------------------------------------

        chart = ChartBuilder.build(
            timestamp=market_start,
            latitude=RESEARCH_LOCATION.latitude,
            longitude=RESEARCH_LOCATION.longitude,
        )

        features = self.feature_builder.build(
            chart,
        )

        # Populate Hora information
        features.hora = hora
        features.hora_number = hora.index
        features.hora_lord = hora.planet

        # -----------------------------------------------------
        # Market
        # -----------------------------------------------------

        market_result = self.market_service.build_between(
            hora=hora,
            start=market_start,
            end=market_end,
        )

        market_features = MarketFeatureBuilder.build(
            open_price=market_result.market.open,
            high_price=market_result.market.high,
            low_price=market_result.market.low,
            close_price=market_result.market.close,
        )

        # -----------------------------------------------------
        # Final Row
        # -----------------------------------------------------

        return ResearchReportRow(
            hora=hora,
            market_start=market_start,
            market_end=market_end,
            chart=chart,
            features=features,
            market=market_result.market,
            market_features=market_features,
        )
    