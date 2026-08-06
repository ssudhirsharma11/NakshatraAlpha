r"""
Statistics CLI
Examples

Show available columns
----------------------

python -m src.research.statistics_cli ^
    --dataset data\market\research_dataset_20210726_20260804.parquet ^
    --columns

Group by one field
------------------

python -m src.research.statistics_cli ^
    --dataset data\market\research_dataset_20210726_20260804.parquet ^
    --group tithi_group

Group by multiple fields
------------------------

python -m src.research.statistics_cli ^
    --dataset data\market\research_dataset_20210726_20260804.parquet ^
    --group tithi_group weekday

Save result
-----------

python -m src.research.statistics_cli ^
    --dataset data\market\research_dataset_20210726_20260804.parquet ^
    --group hora_lord ^
    --output results.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.research.statistics_engine import (
    StatisticsEngine,
)


def build_parser():

    parser = argparse.ArgumentParser(
        description="Nakshatra Alpha Statistics Engine",
    )

    parser.add_argument(
        "--dataset",
        required=True,
        help="Research dataset parquet/csv file",
    )

    parser.add_argument(
        "--group",
        nargs="+",
        help="Column(s) to group by",
    )

    parser.add_argument(
        "--output",
        help="Optional output CSV/Parquet",
    )

    parser.add_argument(
        "--columns",
        action="store_true",
        help="Show available dataset columns",
    )

    return parser


def main():

    args = build_parser().parse_args()

    engine = StatisticsEngine(
        Path(args.dataset),
    )

    if args.columns:

        print()

        print("=" * 70)

        print("Available Columns")

        print("=" * 70)

        for column in engine.available_columns():

            print(column)

        return

    if args.group is None:

        raise SystemExit(
            "--group is required unless using --columns"
        )

    result = engine.group_by(
        args.group,
    )

    print()

    print("=" * 70)

    print(result)

    print("=" * 70)

    print()

    if args.output:

        engine.save(
            result,
            args.output,
        )

        print(
            f"Saved to {args.output}"
        )


if __name__ == "__main__":

    pd.set_option(
        "display.max_columns",
        None,
    )

    pd.set_option(
        "display.width",
        200,
    )

    pd.set_option(
        "display.max_rows",
        500,
    )

    main()