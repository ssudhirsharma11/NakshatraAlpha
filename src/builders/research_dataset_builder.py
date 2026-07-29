"""
Research Dataset Builder

Builds the complete research dataset by combining

- Hora
- Astrological Features
- Market Statistics
"""

from __future__ import annotations

from dataclasses import asdict

import pandas as pd

from src.services.chart_builder import ChartBuilder
from src.features.feature_builder import FeatureBuilder
from src.models.feature_set import FeatureSet
from src.services.hora_market_service import HoraMarketService
from src.services.hora_service import HoraService
from src.services.market_data_service import MarketDataService
from src.config.research_config import RESEARCH_LOCATION


class ResearchDatasetBuilder:
    """
    Builds the complete astrology + market
    research dataset.
    """

    def __init__(
        self,
        market_data_service: MarketDataService | None = None,
        hora_service: HoraService | None = None,
        hora_market_service: HoraMarketService | None = None,
        chart_builder: ChartBuilder | None = None,
        feature_builder: FeatureBuilder | None = None,
    ):

        self.market_data = (
            market_data_service
            or MarketDataService()
        )

        self.hora_service = (
            hora_service
            or HoraService()
        )

        self.hora_market = (
            hora_market_service
            or HoraMarketService(self.market_data)
        )

        self.chart_builder = (
            chart_builder
            or ChartBuilder()
        )

        self.feature_builder = (
            feature_builder
            or FeatureBuilder()
        )

    def build(self) -> pd.DataFrame:
        """
        Builds the research dataframe.

        Returns
        -------
        pandas.DataFrame
        """

        rows = []

        for trading_day in self.market_data.trading_days():

            horas = self.hora_service.get_day_horas(
                calculation_date=trading_day,
                location=RESEARCH_LOCATION,
            )

            for hora in horas:

                try:

                    chart = self.chart_builder.build(
                        timestamp=hora.start,
                        latitude=RESEARCH_LOCATION.latitude,
                        longitude=RESEARCH_LOCATION.longitude,
                    )

                    features: FeatureSet = (
                        self.feature_builder.build(chart)
                    )

                    market = self.hora_market.build(
                        hora
                    )

                    row = self._build_row(
                        hora=hora,
                        features=features,
                        market=market,
                    )

                    rows.append(row)

                except ValueError:
                    #
                    # Ignore Horas having no
                    # market candles.
                    #
                    continue

        return pd.DataFrame(rows)

    def _build_row(
        self,
        hora,
        features,
        market,
    ) -> dict:
        """
        Converts all objects into one flat row.
        """

        row = {}

        # --------------------------------------------------
        # Hora
        # --------------------------------------------------

        row["date"] = hora.start.date()

        row["hora_number"] = hora.index

        row["hora_lord"] = (
            hora.planet.name
            if hora.planet
            else None
        )

        row["hora_start"] = hora.start

        row["hora_end"] = hora.end

        # --------------------------------------------------
        # FeatureSet
        # --------------------------------------------------

        feature_dict = asdict(features)

        for key, value in feature_dict.items():

            if key == "chart":
                continue

            if hasattr(value, "name"):
                row[key] = value.name
            else:
                row[key] = value

        # --------------------------------------------------
        # Market
        # --------------------------------------------------

        row["open"] = market.open
        row["high"] = market.high
        row["low"] = market.low
        row["close"] = market.close

        row["up_move"] = market.up_move
        row["down_move"] = market.down_move
        row["trading_range"] = market.trading_range

        row["candle_count"] = market.candle_count

        row["bullish"] = market.bullish
        row["bearish"] = market.bearish
        row["doji"] = market.doji
        row["body"] = market.body

        return row