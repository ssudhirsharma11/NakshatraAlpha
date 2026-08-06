"""
Market History Downloader

Entry point for downloading historical market data.
"""

from __future__ import annotations

from datetime import date

from src.config.market_config import (
    DEFAULT_SYMBOL,
    DEFAULT_TIMEFRAME,
    DOWNLOAD_BATCH_DAYS,
    EXPORT_CSV,
)
from src.market.history_download_manager import (
    HistoryDownloadManager,
)
from src.market.market_repository import (
    MarketRepository,
)
from src.market.timeframe import Timeframe


# ==========================================================
# CONFIGURATION
# ==========================================================

DOWNLOAD_MODE = "FULL"

# ----------------------------------------------------------
# Instrument
# ----------------------------------------------------------

SYMBOL = DEFAULT_SYMBOL

TIMEFRAME = DEFAULT_TIMEFRAME

# ----------------------------------------------------------
# History Range
# ----------------------------------------------------------

FULL_END_DATE = date.today()

RANGE_START_DATE = date(
    2026,
    1,
    1,
)

RANGE_END_DATE = date(
    2026,
    7,
    17,
)


# ==========================================================
# MAIN
# ==========================================================

def main() -> None:

    print("\n" + "=" * 70)
    print("NAKSHATRA ALPHA MARKET DOWNLOAD")
    print("=" * 70)

    print(f"Mode       : {DOWNLOAD_MODE}")
    print(f"Instrument : {SYMBOL}")
    print(f"Timeframe  : {TIMEFRAME.name}")

    repo = MarketRepository()

    manager = HistoryDownloadManager(
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        batch_days=DOWNLOAD_BATCH_DAYS,
    )

    start_date = (
        date(2000, 1, 1)
        if TIMEFRAME == Timeframe.DAILY
        else date(2015, 1, 1)
    )

    parquet_file = repo.parquet_file(
        SYMBOL,
        TIMEFRAME,
    )

    csv_file = (
        repo.csv_file(
            SYMBOL,
            TIMEFRAME,
        )
        if EXPORT_CSV
        else None
    )

    if DOWNLOAD_MODE == "FULL":

        manager.download_full(
            start=start_date,
            end=FULL_END_DATE,
            parquet_file=parquet_file,
            csv_file=csv_file,
        )

    elif DOWNLOAD_MODE == "UPDATE":

        manager.update(
            parquet_file=parquet_file,
            csv_file=csv_file,
        )

    elif DOWNLOAD_MODE == "RANGE":

        manager.download_full(
            start=RANGE_START_DATE,
            end=RANGE_END_DATE,
            parquet_file=parquet_file,
            csv_file=csv_file,
        )

    else:

        raise ValueError(
            f"Unsupported DOWNLOAD_MODE: {DOWNLOAD_MODE}"
        )

    print("\n" + "=" * 70)
    print("DOWNLOAD COMPLETED")
    print("=" * 70 + "\n")


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()