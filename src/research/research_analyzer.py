"""
research_analyzer.py

NakshatraAlpha Research Analyzer

Loads the research dataset and generates statistical reports for
astrological and market features.

Author: Sudhir Sharma / NakshatraAlpha
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any

import numpy as np
import pandas as pd


class ResearchAnalyzer:
    """
    Performs statistical analysis on the research dataset.
    """

    REQUIRED_COLUMNS = [
        "return_pct",
        "trading_range",
        "body_pct",
        "upper_wick_pct",
        "lower_wick_pct",
        "close_position_pct",
        "up_move",
        "down_move",
        "high_volatility",
        "low_volatility",
    ]

    ANALYSIS_COLUMNS = [
        "hora_lord",
        "weekday",
        "tithi",
        "paksha",
        "moon_nakshatra",
        "sun_nakshatra",
        "lagna_sign",
        "sun_sign",
        "moon_sign",
        "direction",
        "strength",
        "sade_sati",
        "sade_sati_phase",
    ]

    def __init__(self) -> None:

        self.project_root = Path(__file__).resolve().parents[2]

        self.dataset_path = (
            self.project_root
            / "data"
            / "research"
            / "research_dataset.csv"
        )

        self.output_dir = (
            self.project_root
            / "data"
            / "research"
            / "reports"
        )

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.df: pd.DataFrame | None = None

    # ---------------------------------------------------------
    # DATASET
    # ---------------------------------------------------------

    def load_dataset(self) -> None:

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found:\n{self.dataset_path}"
            )

        self.df = pd.read_csv(self.dataset_path)

        self._validate_dataset()

        print("=" * 60)
        print("NAKSHATRAALPHA RESEARCH ANALYZER")
        print("=" * 60)

        print(f"Dataset : {self.dataset_path.name}")
        print(f"Rows    : {len(self.df):,}")
        print(f"Columns : {len(self.df.columns)}")

        print()

    def _validate_dataset(self) -> None:

        if self.df is None:
            raise ValueError("Dataset not loaded.")

        missing = []

        for column in self.REQUIRED_COLUMNS:
            if column not in self.df.columns:
                missing.append(column)

        if missing:

            raise ValueError(
                "Missing required columns:\n"
                + "\n".join(missing)
            )

    # ---------------------------------------------------------
    # MARKET SUMMARY
    # ---------------------------------------------------------

    def market_summary(self) -> pd.DataFrame:

        assert self.df is not None

        total_rows = len(self.df)

        summary = {

            "Metric": [

                "Total Samples",
                "Average Return %",
                "Median Return %",
                "Std Dev Return %",
                "Largest Gain %",
                "Largest Loss %",
                "Average Trading Range",
                "Median Trading Range",
                "Average Body %",
                "Average Upper Wick %",
                "Average Lower Wick %",
                "Average Close Position %",
                "Average Up Move",
                "Average Down Move",
                "Win Rate %",
                "High Volatility %",
                "Low Volatility %",

            ],

            "Value": [

                total_rows,

                self.df["return_pct"].mean(),

                self.df["return_pct"].median(),

                self.df["return_pct"].std(),

                self.df["return_pct"].max(),

                self.df["return_pct"].min(),

                self.df["trading_range"].mean(),

                self.df["trading_range"].median(),

                self.df["body_pct"].mean(),

                self.df["upper_wick_pct"].mean(),

                self.df["lower_wick_pct"].mean(),

                self.df["close_position_pct"].mean(),

                self.df["up_move"].mean(),

                self.df["down_move"].mean(),

                (
                    (
                        self.df["return_pct"] > 0
                    ).mean()
                    * 100
                ),

                (
                    self.df["high_volatility"]
                    .astype(int)
                    .mean()
                    * 100
                ),

                (
                    self.df["low_volatility"]
                    .astype(int)
                    .mean()
                    * 100
                ),

            ],
        }

        market_df = pd.DataFrame(summary)

        output_file = (
            self.output_dir
            / "market_summary.csv"
        )

        market_df.to_csv(
            output_file,
            index=False,
        )

        print("Market Summary")
        print("-" * 60)

        for _, row in market_df.iterrows():

            metric = row["Metric"]

            value = row["Value"]

            if isinstance(value, (float, np.floating)):
                print(f"{metric:<30} : {value:.2f}")
            else:
                print(f"{metric:<30} : {value}")

        print()

        return market_df

    # ---------------------------------------------------------
    # GENERIC STATISTICS
    # ---------------------------------------------------------

    @staticmethod
    def _win_rate(series: pd.Series) -> float:

        return (series > 0).mean() * 100

    @staticmethod
    def _safe_mean(series: pd.Series) -> float:

        if len(series) == 0:
            return 0.0

        return float(series.mean())

    @staticmethod
    def _safe_median(series: pd.Series) -> float:

        if len(series) == 0:
            return 0.0

        return float(series.median())

    @staticmethod
    def _safe_std(series: pd.Series) -> float:

        if len(series) <= 1:
            return 0.0

        return float(series.std())
        # ---------------------------------------------------------
    # GROUP ANALYSIS
    # ---------------------------------------------------------

    def analyze(self, column: str) -> pd.DataFrame:

        """
        Generic analysis function.

        Example:

            analyze("hora_lord")
            analyze("weekday")
            analyze("tithi")
        """

        assert self.df is not None

        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found.")

        grouped = self.df.groupby(column, dropna=False)

        rows: List[Dict[str, Any]] = []

        for value, group in grouped:

            value_name = "UNKNOWN" if pd.isna(value) else str(value)

            samples = len(group)

            return_series = group["return_pct"]

            win_rate = self._win_rate(return_series)

            row = {

                column: value_name,

                "samples": samples,

                "avg_return_pct":
                    self._safe_mean(return_series),

                "median_return_pct":
                    self._safe_median(return_series),

                "std_return_pct":
                    self._safe_std(return_series),

                "max_gain_pct":
                    float(return_series.max()),

                "max_loss_pct":
                    float(return_series.min()),

                "win_rate":
                    win_rate,

                "positive_count":
                    int((return_series > 0).sum()),

                "negative_count":
                    int((return_series < 0).sum()),

                "average_trading_range":
                    self._safe_mean(group["trading_range"]),

                "average_body_pct":
                    self._safe_mean(group["body_pct"]),

                "average_upper_wick_pct":
                    self._safe_mean(group["upper_wick_pct"]),

                "average_lower_wick_pct":
                    self._safe_mean(group["lower_wick_pct"]),

                "average_close_position_pct":
                    self._safe_mean(group["close_position_pct"]),

                "average_up_move":
                    self._safe_mean(group["up_move"]),

                "average_down_move":
                    self._safe_mean(group["down_move"]),

                "high_volatility_pct":
                    (
                        group["high_volatility"]
                        .astype(int)
                        .mean()
                        * 100
                    ),

                "low_volatility_pct":
                    (
                        group["low_volatility"]
                        .astype(int)
                        .mean()
                        * 100
                    ),
            }

            rows.append(row)

        report = pd.DataFrame(rows)

        report = self._rank_report(report)

        self._save_report(
            report,
            f"{column}_summary.csv",
        )

        print(f"[OK] {column:<20} ({len(report)} groups)")

        return report

    # ---------------------------------------------------------
    # REPORT RANKING
    # ---------------------------------------------------------

    @staticmethod
    def _rank_report(
        report: pd.DataFrame,
    ) -> pd.DataFrame:

        """
        Rank results by:

        1. Win Rate
        2. Average Return
        3. Sample Size
        """

        return (
            report
            .sort_values(
                by=[
                    "win_rate",
                    "avg_return_pct",
                    "samples",
                ],
                ascending=[
                    False,
                    False,
                    False,
                ],
            )
            .reset_index(drop=True)
        )

    # ---------------------------------------------------------
    # CSV EXPORT
    # ---------------------------------------------------------

    def _save_report(
        self,
        report: pd.DataFrame,
        filename: str,
    ) -> None:

        output_file = self.output_dir / filename

        report.to_csv(
            output_file,
            index=False,
        )

    # ---------------------------------------------------------
    # ANALYZE ALL CONFIGURED COLUMNS
    # ---------------------------------------------------------

    def analyze_all(self) -> None:

        print("=" * 60)
        print("GENERATING REPORTS")
        print("=" * 60)

        for column in self.ANALYSIS_COLUMNS:

            try:

                self.analyze(column)

            except Exception as exc:

                print(
                    f"[SKIPPED] {column} : {exc}"
                )

        print()
            # ---------------------------------------------------------
    # MAIN EXECUTION
    # ---------------------------------------------------------

    def run(self) -> None:

        print()
        print("=" * 60)
        print("STARTING RESEARCH ANALYSIS")
        print("=" * 60)
        print()

        self.load_dataset()

        print("=" * 60)
        print("MARKET SUMMARY")
        print("=" * 60)

        self.market_summary()

        self.analyze_all()

        print("=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)

        print(f"Dataset           : {self.dataset_path.name}")
        print(f"Rows              : {len(self.df):,}")
        print(f"Reports Generated : {len(self.ANALYSIS_COLUMNS) + 1}")
        print(f"Output Folder     : {self.output_dir}")

        print()

        print("Generated Reports")

        reports = sorted(self.output_dir.glob("*.csv"))

        for report in reports:
            print(f"  - {report.name}")

        print()
        print("=" * 60)
        print("RESEARCH ANALYZER FINISHED")
        print("=" * 60)
        print()


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main() -> None:

    try:

        analyzer = ResearchAnalyzer()

        analyzer.run()

    except KeyboardInterrupt:

        print()
        print("[INTERRUPTED] Analysis cancelled by user.")

    except Exception as exc:

        print()
        print("=" * 60)
        print("ERROR")
        print("=" * 60)
        print(type(exc).__name__)
        print(exc)
        print()


if __name__ == "__main__":

    main()