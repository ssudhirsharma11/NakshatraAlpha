"""
Dataset Enricher

Adds derived market statistics to the raw research dataset.

All market calculations are delegated to
MarketFeatureBuilder.

The enricher is now responsible only for
DataFrame orchestration.
"""

from __future__ import annotations

from dataclasses import asdict

import pandas as pd

from src.features.market_feature_builder import (
    MarketFeatureBuilder,
)


class DatasetEnricher:
    """
    Enriches the raw dataset with
    derived market features.
    """

    def enrich(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df = df.copy()

        # ---------------------------------------------
        # Dataset Median (required for volatility)
        # ---------------------------------------------

        temp_range = (
            (df["high"] - df["low"])
            / df["open"]
        ) * 100

        median_range_pct = temp_range.median()

        rows = []

        for _, row in df.iterrows():

            features = MarketFeatureBuilder.build(

                open_price=row["open"],

                high_price=row["high"],

                low_price=row["low"],

                close_price=row["close"],

                median_range_pct=median_range_pct,

            )

            row_dict = row.to_dict()

            row_dict.update(
                asdict(features)
            )

            rows.append(row_dict)

        return pd.DataFrame(rows)