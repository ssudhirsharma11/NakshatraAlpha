"""
Research Dataset Builder

Builds the complete research dataset by combining

- Hora
- Astrological Features
- Market Statistics

The builder returns a pandas DataFrame.
Saving to CSV is handled elsewhere.
"""

from __future__ import annotations

from dataclasses import asdict
from enum import Enum

import pandas as pd

from src.config.research_config import RESEARCH_LOCATION
from src.features.feature_builder import FeatureBuilder
from src.features.market_feature_builder import MarketFeatureBuilder
from src.services.chart_builder import ChartBuilder
from src.services.hora_market_service import HoraMarketService
from src.services.hora_service import HoraService
from src.services.market_data_service import MarketDataService


class DatasetBuilder:
    """
    Builds the complete astrology research dataset.
    """

    def __init__(
        self,
        market_data_service: MarketDataService | None = None,
        hora_service: HoraService | None = None,
        hora_market_service: HoraMarketService | None = None,
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

        self.feature_builder = FeatureBuilder()

    def build(self) -> pd.DataFrame:
        """
        Build the complete research dataset.
        """

        rows: list[dict] = []

        trading_days = self.market_data.trading_days()

        print(
            f"\nBuilding dataset for "
            f"{len(trading_days)} trading days...\n"
        )

        skipped = 0

        for trading_day in trading_days:

            horas = self.hora_service.get_day_horas(
                calculation_date=trading_day,
                location=RESEARCH_LOCATION,
            )

            for hora in horas:

                try:

                    chart = ChartBuilder.build(
                        timestamp=hora.start,
                        latitude=RESEARCH_LOCATION.latitude,
                        longitude=RESEARCH_LOCATION.longitude,
                    )

                    features = self.feature_builder.build(
                        chart
                    )

                    market_result = self.hora_market.build(
                        hora
                    )

                    market_features = MarketFeatureBuilder.build(
                        open_price=market_result.market.open,
                        high_price=market_result.market.high,
                        low_price=market_result.market.low,
                        close_price=market_result.market.close,
                    )

                    rows.append(
                        self._create_row(
                            hora=hora,
                            features=features,
                            market=market_result.market,
                            market_features=market_features,
                        )
                    )

                except Exception as ex:

                    skipped += 1

                    print(
                        f"Skipped {hora.start} : {ex}"
                    )

        df = pd.DataFrame(rows)

        print("\nCompleted.")
        print(f"Rows    : {len(df)}")
        print(f"Skipped : {skipped}")

        return df

    def _create_row(
        self,
        hora,
        features,
        market,
        market_features,
    ) -> dict:

        row: dict = {}

        # -------------------------------------------------
        # Hora
        # -------------------------------------------------

        row["date"] = hora.start.date()

        row["hora_number"] = hora.index
        row["hora_lord"] = hora.planet.name

        row["hora_start"] = hora.start
        row["hora_end"] = hora.end

        row["is_day_hora"] = hora.is_day

        # -------------------------------------------------
        # Astrology
        # -------------------------------------------------

        feature_dict = asdict(features)

        ignored_fields = {
            "chart",
            "hora",
            "hora_number",
            "hora_lord",
        }

        for key, value in feature_dict.items():

            if key in ignored_fields:
                continue

            if isinstance(value, Enum):
                row[key] = value.name

            elif hasattr(value, "name"):
                row[key] = value.name

            else:
                row[key] = value

        # -------------------------------------------------
        # Raw Market Data
        # -------------------------------------------------

        row["open"] = market.open
        row["high"] = market.high
        row["low"] = market.low
        row["close"] = market.close

        row["up_move"] = market.up_move
        row["down_move"] = market.down_move
        row["trading_range"] = market.trading_range
        row["candle_count"] = market.candle_count

        # -------------------------------------------------
        # Derived Market Features
        # -------------------------------------------------

        row["return_pct"] = market_features.return_pct
        row["direction"] = market_features.direction
        row["strength"] = market_features.strength
        row["body"] = market_features.body
        row["trading_range"] = market_features.trading_range

        return row