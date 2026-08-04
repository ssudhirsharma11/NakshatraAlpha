"""
History Download Manager

Downloads complete historical market data
using multiple Kite API requests.

Responsibilities

- Split large date ranges into batches
- Download each batch
- Merge results
- Validate data
- Save locally
- Update existing database
"""

from __future__ import annotations

from datetime import date
from datetime import datetime
from datetime import timedelta

import pandas as pd

from src.market.providers.kite_provider import KiteProvider
from src.market.timeframe import Timeframe


class HistoryDownloadManager:
    """
    Downloads historical market data in batches
    using KiteProvider.
    """

    def __init__(
        self,
        symbol: str,
        timeframe: Timeframe,
        batch_days: int = 180,
    ):

        self.symbol = symbol.upper()

        self.timeframe = timeframe

        self.batch_days = batch_days

        self.provider = KiteProvider()

    # =====================================================
    # PUBLIC
    # =====================================================

    def download_range(
        self,
        start: date,
        end: date,
    ) -> pd.DataFrame:
        """
        Download an arbitrary date range.

        Large ranges are automatically split into
        multiple Kite API requests.
        """

        batches = self._create_batches(
            start,
            end,
        )

        all_frames: list[pd.DataFrame] = []

        total = len(batches)

        print("\n" + "=" * 70)
        print("NAKSHATRA ALPHA DOWNLOAD")
        print("=" * 70)

        print(f"Instrument : {self.symbol}")
        print(f"Timeframe  : {self.timeframe.name}")
        print(f"Batches    : {total}\n")

        for index, (batch_start, batch_end) in enumerate(
            batches,
            start=1,
        ):

            print(
                f"[{index}/{total}] "
                f"{batch_start} -> {batch_end}"
            )

            frame = self._download_batch_with_retry(
                batch_start,
                batch_end,
            )

            print(
                f"Downloaded : {len(frame):,} candles\n"
            )

            all_frames.append(frame)

        return self._merge_batches(
            all_frames
        )

    # =====================================================
    # INTERNAL
    # =====================================================

    def _create_batches(
        self,
        start: date,
        end: date,
    ) -> list[tuple[date, date]]:
        """
        Split a large date range into
        smaller download batches.
        """

        batches: list[tuple[date, date]] = []

        current = start

        while current <= end:

            batch_end = min(
                current
                + timedelta(
                    days=self.batch_days - 1,
                ),
                end,
            )

            batches.append(
                (
                    current,
                    batch_end,
                )
            )

            current = batch_end + timedelta(
                days=1,
            )

        return batches    
    def _download_batch(
        self,
        start: date,
        end: date,
    ) -> pd.DataFrame:
        """
        Download one batch from Kite.
        """

        dataset = self.provider.download(

            symbol=self.symbol,

            timeframe=self.timeframe,

            start=datetime.combine(
                start,
                datetime.min.time(),
            ),

            end=datetime.combine(
                end,
                datetime.max.time(),
            ),
        )

        rows: list[dict] = []

        for bar in dataset:

            rows.append(

                {
                    "timestamp": bar.timestamp,
                    "open": bar.open,
                    "high": bar.high,
                    "low": bar.low,
                    "close": bar.close,
                    "volume": bar.volume,
                }

            )

        return pd.DataFrame(rows)

    def _download_batch_with_retry(
        self,
        start: date,
        end: date,
        retries: int = 3,
    ) -> pd.DataFrame:
        """
        Download a batch with automatic retry.
        """

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                return self._download_batch(
                    start,
                    end,
                )

            except Exception as ex:

                last_error = ex

                print(
                    f"Retry {attempt}/{retries} failed: {ex}"
                )

        raise RuntimeError(
            f"Failed downloading batch "
            f"{start} -> {end}"
        ) from last_error

    def _merge_batches(
        self,
        frames: list[pd.DataFrame],
    ) -> pd.DataFrame:
        """
        Merge all downloaded batches into
        one sorted dataframe.
        """

        if not frames:

            return pd.DataFrame()

        df = pd.concat(
            frames,
            ignore_index=True,
        )

        df.sort_values(
            "timestamp",
            inplace=True,
        )

        df.drop_duplicates(
            subset=["timestamp"],
            inplace=True,
        )

        df.reset_index(
            drop=True,
            inplace=True,
        )

        return df    # =====================================================
    # SAVE
    # =====================================================

    def save(
        self,
        df: pd.DataFrame,
        parquet_file,
        csv_file=None,
    ) -> None:
        """
        Save downloaded data.
        """

        print("\nSaving data...\n")

        parquet_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_parquet(
            parquet_file,
            index=False,
        )

        print(
            f"✓ Parquet saved : {parquet_file}"
        )

        if csv_file is not None:

            df.to_csv(
                csv_file,
                index=False,
            )

            print(
                f"✓ CSV saved     : {csv_file}"
            )

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Validate downloaded market data.
        """

        if df.empty:

            raise ValueError(
                "Downloaded dataframe is empty."
            )

        required = [
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        for column in required:

            if column not in df.columns:

                raise ValueError(
                    f"Missing column '{column}'."
                )

        duplicates = df.duplicated(
            subset=["timestamp"]
        ).sum()

        if duplicates:

            raise ValueError(
                f"{duplicates} duplicate timestamps detected."
            )

        if not df["timestamp"].is_monotonic_increasing:

            raise ValueError(
                "Timestamps are not sorted."
            )

        if df[
            [
                "open",
                "high",
                "low",
                "close",
            ]
        ].isnull().any().any():

            raise ValueError(
                "OHLC contains null values."
            )

        if (df["high"] < df["low"]).any():

            raise ValueError(
                "Invalid candles found (High < Low)."
            )

        print("✓ Validation passed")

    # =====================================================
    # SUMMARY
    # =====================================================

    def print_summary(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Print download summary.
        """

        trading_days = (
            df["timestamp"]
            .dt.date
            .nunique()
        )

        print("\n" + "=" * 70)
        print("DOWNLOAD SUMMARY")
        print("=" * 70)

        print(f"Instrument    : {self.symbol}")

        print(
            f"Rows          : {len(df):,}"
        )

        print(
            f"Trading Days  : {trading_days:,}"
        )

        print(
            f"Candles/Day   : "
            f"{len(df)/trading_days:.1f}"
        )

        print(
            f"From          : "
            f"{df.iloc[0]['timestamp']}"
        )

        print(
            f"To            : "
            f"{df.iloc[-1]['timestamp']}"
        )

        print(
            f"Duplicates    : "
            f"{df.duplicated(subset=['timestamp']).sum()}"
        )

        print("=" * 70 + "\n")    # =====================================================
    # FULL DOWNLOAD
    # =====================================================

    def download_full(
        self,
        start: date,
        end: date,
        parquet_file,
        csv_file=None,
    ) -> pd.DataFrame:
        """
        Download the complete date range,
        validate it and save it.
        """

        df = self.download_range(
            start,
            end,
        )

        self.validate(
            df,
        )

        self.save(
            df,
            parquet_file,
            csv_file,
        )

        self.print_summary(
            df,
        )

        return df

    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        parquet_file,
        csv_file=None,
    ) -> pd.DataFrame:
        """
        Update an existing historical database.

        Starts downloading from the last available
        trading day and relies on duplicate removal
        to avoid duplicate candles.
        """

        if not parquet_file.exists():

            raise FileNotFoundError(
                "Parquet file not found. "
                "Run a full download first."
            )

        existing = pd.read_parquet(
            parquet_file,
        )

        if existing.empty:

            raise ValueError(
                "Existing parquet file is empty."
            )

        last_timestamp = existing.iloc[-1][
            "timestamp"
        ]

        print(
            "\nExisting database ends at:"
        )

        print(last_timestamp)

        # ---------------------------------------------
        # Download again from the same day.
        # Duplicate timestamps are removed later.
        # This protects against partial downloads.
        # ---------------------------------------------

        start = last_timestamp.date()

        end = date.today()

        if start > end:

            print(
                "\nDatabase already up-to-date."
            )

            return existing

        new = self.download_range(
            start,
            end,
        )

        merged = pd.concat(
            [
                existing,
                new,
            ],
            ignore_index=True,
        )

        merged.sort_values(
            "timestamp",
            inplace=True,
        )

        merged.drop_duplicates(
            subset=["timestamp"],
            inplace=True,
        )

        merged.reset_index(
            drop=True,
            inplace=True,
        )

        self.validate(
            merged,
        )

        self.save(
            merged,
            parquet_file,
            csv_file,
        )

        self.print_summary(
            merged,
        )

        return merged