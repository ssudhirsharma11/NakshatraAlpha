"""
Statistics Engine

Performs statistical analysis on the Nakshatra Alpha
research dataset.

The engine is intentionally generic.

Examples
--------

engine.group_by("tithi_group")

engine.group_by("weekday")

engine.group_by(
    ["tithi_group", "weekday"]
)

engine.group_by(
    ["hora_lord", "moon_nakshatra"]
)
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class StatisticsEngine:
    """
    Generic statistics engine.

    Loads the exported research dataset and
    computes grouped statistics.
    """

    # ---------------------------------------------------------
    # Construction
    # ---------------------------------------------------------

    def __init__(
        self,
        dataset_file: str | Path,
    ):

        self.dataset_file = Path(
            dataset_file,
        )

        if not self.dataset_file.exists():

            raise FileNotFoundError(
                self.dataset_file
            )

        self.df = pd.read_parquet(
            self.dataset_file,
        )

    # ---------------------------------------------------------
    # Information
    # ---------------------------------------------------------

    @property
    def columns(
        self,
    ) -> list[str]:

        return sorted(
            self.df.columns.tolist()
        )

    @property
    def total_rows(
        self,
    ) -> int:

        return len(
            self.df
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate_columns(
        self,
        columns: list[str],
    ):

        missing = [

            column

            for column in columns

            if column not in self.df.columns

        ]

        if missing:

            raise ValueError(

                "Unknown columns: "

                + ", ".join(missing)

            )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _prepare_groups(
        self,
        group_by,
    ) -> list[str]:

        if isinstance(
            group_by,
            str,
        ):

            columns = [
                group_by,
            ]

        else:

            columns = list(
                group_by,
            )

        self.validate_columns(
            columns,
        )

        return columns

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    @staticmethod
    def save(
        df: pd.DataFrame,
        output_file: str | Path,
    ):

        output_file = Path(
            output_file,
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if output_file.suffix.lower() == ".csv":

            df.to_csv(
                output_file,
                index=False,
            )

        elif output_file.suffix.lower() == ".parquet":

            df.to_parquet(
                output_file,
                index=False,
            )

        else:

            raise ValueError(
                "Unsupported file format."
            )    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def group_by(
        self,
        group_by,
    ) -> pd.DataFrame:

        columns = self._prepare_groups(
            group_by,
        )

        df = self.df.copy()

        df["bullish"] = (
            df["return_pct"] > 0
        )

        df["bearish"] = (
            df["return_pct"] < 0
        )

        df["neutral"] = (
            df["return_pct"] == 0
        )

        df["strong_bull"] = (
            df["strength"] == "Strong Bull"
        )

        df["strong_bear"] = (
            df["strength"] == "Bear"
        )

        result = (

            df.groupby(
                columns,
                dropna=False,
            )

            .agg(

                sample_size=(
                    "research_id",
                    "count",
                ),

                bullish_pct=(
                    "bullish",
                    "mean",
                ),

                bearish_pct=(
                    "bearish",
                    "mean",
                ),

                neutral_pct=(
                    "neutral",
                    "mean",
                ),

                average_return_pct=(
                    "return_pct",
                    "mean",
                ),

                median_return_pct=(
                    "return_pct",
                    "median",
                ),

                average_range=(
                    "trading_range",
                    "mean",
                ),

                average_body=(
                    "body",
                    "mean",
                ),

                average_up_move=(
                    "up_move",
                    "mean",
                ),

                average_down_move=(
                    "down_move",
                    "mean",
                ),

                strong_bull_pct=(
                    "strong_bull",
                    "mean",
                ),

                strong_bear_pct=(
                    "strong_bear",
                    "mean",
                ),

                average_candles=(
                    "candle_count",
                    "mean",
                ),

            )

            .reset_index()

        )

        percent_columns = [

            "bullish_pct",

            "bearish_pct",

            "neutral_pct",

            "strong_bull_pct",

            "strong_bear_pct",

        ]

        for column in percent_columns:

            result[column] = (
                result[column] * 100
            ).round(
                2,
            )

        numeric_columns = [

            "average_return_pct",

            "median_return_pct",

            "average_range",

            "average_body",

            "average_up_move",

            "average_down_move",

            "average_candles",

        ]

        result[
            numeric_columns
        ] = result[
            numeric_columns
        ].round(
            2,
        )

        result = result.sort_values(

            by="average_return_pct",

            ascending=False,

        )

        result = result.reset_index(
            drop=True,
        )

        return result    # ---------------------------------------------------------
    # Convenience Methods
    # ---------------------------------------------------------

    def top(
        self,
        group_by,
        n: int = 10,
    ) -> pd.DataFrame:
        """
        Returns the top N groups ranked by
        average return.
        """

        return self.group_by(
            group_by,
        ).head(
            n,
        )

    def bottom(
        self,
        group_by,
        n: int = 10,
    ) -> pd.DataFrame:
        """
        Returns the bottom N groups ranked by
        average return.
        """

        return self.group_by(
            group_by,
        ).tail(
            n,
        )

    def filter(
        self,
        **conditions,
    ) -> pd.DataFrame:
        """
        Returns rows matching one or more
        conditions.

        Example

        filter(
            tithi_group="BHADRA",
            weekday="Tuesday",
        )
        """

        df = self.df.copy()

        for column, value in conditions.items():

            if column not in df.columns:

                raise ValueError(
                    f"Unknown column: {column}"
                )

            df = df[
                df[column] == value
            ]

        return df.reset_index(
            drop=True,
        )

    def available_columns(
        self,
    ) -> list[str]:

        return self.columns

    def describe(
        self,
    ) -> dict:

        return {

            "rows": len(
                self.df,
            ),

            "columns": len(
                self.df.columns,
            ),

            "first_date": self.df[
                "trading_date"
            ].min(),

            "last_date": self.df[
                "trading_date"
            ].max(),

            "column_names": self.columns,

        }