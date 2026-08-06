"""
Export Research Dataset

Examples

Single Day
----------

python -m src.research.export_dataset --day 2025-03-10

Date Range
----------

python -m src.research.export_dataset ^
    --start 2021-07-24 ^
    --end 2026-08-06
"""

from __future__ import annotations

import argparse
from datetime import date
from datetime import datetime

from src.config.market_config import MARKET_DATA_DIR
from src.research.research_dataset_exporter import (
    ResearchDatasetExporter,
)


def parse_date(value: str) -> date:

    return datetime.strptime(
        value,
        "%Y-%m-%d",
    ).date()


def build_parser():

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(
        required=True,
    )

    group.add_argument(
        "--day",
        type=parse_date,
    )

    group.add_argument(
        "--start",
        type=parse_date,
    )

    parser.add_argument(
        "--end",
        type=parse_date,
    )

    parser.add_argument(
        "--hora",
        type=int,
        choices=range(1, 13),
    )

    return parser


def main():

    parser = build_parser()

    args = parser.parse_args()

    exporter = ResearchDatasetExporter()

    if args.day:

        df = exporter.export_day(
            args.day,
            args.hora,
        )

        name = args.day.strftime(
            "%Y%m%d"
        )

    else:

        if args.end is None:

            parser.error(
                "--start requires --end"
            )

        df = exporter.export_range(
            args.start,
            args.end,
            args.hora,
        )

        name = (
            f"{args.start:%Y%m%d}"
            "_"
            f"{args.end:%Y%m%d}"
        )

    parquet_file = (
        MARKET_DATA_DIR /
        f"research_dataset_{name}.parquet"
    )

    csv_file = (
        MARKET_DATA_DIR /
        f"research_dataset_{name}.csv"
    )

    exporter.save(
        df,
        parquet_file,
        csv_file,
    )

    print()

    print("=" * 70)

    print(
        f"Rows      : {len(df):,}"
    )

    print(
        f"Columns   : {len(df.columns)}"
    )

    print(
        f"Parquet   : {parquet_file}"
    )

    print(
        f"CSV       : {csv_file}"
    )

    print("=" * 70)


if __name__ == "__main__":

    main()