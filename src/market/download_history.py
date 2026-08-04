"""
Market History Downloader

Entry point for downloading historical market data.

Supported modes

- FULL
- UPDATE
- RANGE
"""

from __future__ import annotations

from datetime import date

from src.config.market_config import (
    CSV_FILE,
    DEFAULT_SYMBOL,
    DEFAULT_TIMEFRAME,
    DOWNLOAD_BATCH_DAYS,
    EXPORT_CSV,
    HISTORY_START_DATE,
    PARQUET_FILE,
)
from src.market.history_download_manager import (
    HistoryDownloadManager,
)


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
# Full Download
# ----------------------------------------------------------

FULL_START_DATE = HISTORY_START_DATE

FULL_END_DATE = date.today()

# ----------------------------------------------------------
# Range Download
# ----------------------------------------------------------

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

    manager = HistoryDownloadManager(
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        batch_days=DOWNLOAD_BATCH_DAYS,
    )

    csv_output = (
        CSV_FILE
        if EXPORT_CSV
        else None
    )

    if DOWNLOAD_MODE == "FULL":

        manager.download_full(
            start=FULL_START_DATE,
            end=FULL_END_DATE,
            parquet_file=PARQUET_FILE,
            csv_file=csv_output,
        )

    elif DOWNLOAD_MODE == "UPDATE":

        manager.update(
            parquet_file=PARQUET_FILE,
            csv_file=csv_output,
        )

    elif DOWNLOAD_MODE == "RANGE":

        manager.download_full(
            start=RANGE_START_DATE,
            end=RANGE_END_DATE,
            parquet_file=PARQUET_FILE,
            csv_file=csv_output,
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