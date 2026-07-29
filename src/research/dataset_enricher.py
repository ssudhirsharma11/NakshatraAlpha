"""
Dataset Enricher

Adds derived market statistics to the raw research dataset.

This class never modifies the input DataFrame.
A new enriched DataFrame is returned.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class DatasetEnricher:
    """
    Enriches the raw dataset with derived market features.
    """

    def enrich(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Returns an enriched copy of the dataset.
        """

        df = df.copy()

        # ----------------------------------------------------
        # Basic Price Components
        # ----------------------------------------------------

        df["body"] = (df["close"] - df["open"]).abs()

        df["range"] = df["high"] - df["low"]

        df["upper_wick"] = (
            df["high"] -
            np.maximum(df["open"], df["close"])
        )

        df["lower_wick"] = (
            np.minimum(df["open"], df["close"]) -
            df["low"]
        )

        # ----------------------------------------------------
        # Percentage Metrics
        # ----------------------------------------------------

        df["return_pct"] = (
            (df["close"] - df["open"])
            / df["open"]
        ) * 100

        df["range_pct"] = (
            df["range"]
            / df["open"]
        ) * 100

        df["body_pct"] = np.where(
            df["range"] == 0,
            0,
            (df["body"] / df["range"]) * 100,
        )

        df["upper_wick_pct"] = np.where(
            df["range"] == 0,
            0,
            (df["upper_wick"] / df["range"]) * 100,
        )

        df["lower_wick_pct"] = np.where(
            df["range"] == 0,
            0,
            (df["lower_wick"] / df["range"]) * 100,
        )

        # ----------------------------------------------------
        # Candle Position
        # ----------------------------------------------------

        df["close_position_pct"] = np.where(
            df["range"] == 0,
            50,
            (
                (df["close"] - df["low"])
                / df["range"]
            ) * 100,
        )

        df["open_position_pct"] = np.where(
            df["range"] == 0,
            50,
            (
                (df["open"] - df["low"])
                / df["range"]
            ) * 100,
        )

        # ----------------------------------------------------
        # Direction
        # ----------------------------------------------------

        df["direction"] = np.select(
            [
                df["close"] > df["open"],
                df["close"] < df["open"],
            ],
            [
                "Bullish",
                "Bearish",
            ],
            default="Neutral",
        )

        # ----------------------------------------------------
        # Strength Classification
        # ----------------------------------------------------

        conditions = [
            df["return_pct"] >= 0.50,
            (df["return_pct"] >= 0.20) &
            (df["return_pct"] < 0.50),

            (df["return_pct"] > -0.20) &
            (df["return_pct"] < 0.20),

            (df["return_pct"] <= -0.20) &
            (df["return_pct"] > -0.50),

            df["return_pct"] <= -0.50,
        ]

        labels = [
            "Strong Bull",
            "Bull",
            "Neutral",
            "Bear",
            "Strong Bear",
        ]

        df["strength"] = np.select(
            conditions,
            labels,
            default="Neutral",
        )

        # ----------------------------------------------------
        # Volatility
        # ----------------------------------------------------

        median_range = df["range_pct"].median()

        df["high_volatility"] = (
            df["range_pct"] >= median_range
        )

        df["low_volatility"] = (
            df["range_pct"] < median_range
        )

        return df