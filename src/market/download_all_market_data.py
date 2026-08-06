"""
Download Entire Market Universe

Downloads all required NSE indices for Nakshatra Alpha.

Features

- MarketUniverse driven
- MarketRepository driven
- Automatic history start date
- Resume support
- Skip existing files
- Download status logging
"""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

from src.config.market_config import (
    DOWNLOAD_BATCH_DAYS,
    EXPORT_CSV,
)

from src.config.market_universe import (
    MARKET_UNIVERSE,
)

from src.market.history_download_manager import (
    HistoryDownloadManager,
)

from src.market.market_repository import (
    MarketRepository,
)

from src.market.timeframe import (
    Timeframe,
)


# ==========================================================
# CONFIGURATION
# ==========================================================

END_DATE = date.today()

DOWNLOAD_LOG = Path(
    "data/market/download_status.csv"
)

REPOSITORY = MarketRepository()


# ==========================================================
# TIMEFRAMES
# ==========================================================

TIMEFRAMES = [

    Timeframe.MINUTE_5,

    Timeframe.DAILY,

]


# ==========================================================
# LOGGING
# ==========================================================

def write_log(
    symbol: str,
    timeframe: Timeframe,
    status: str,
    rows: int = 0,
    error: str = "",
) -> None:

    DOWNLOAD_LOG.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    first_write = not DOWNLOAD_LOG.exists()

    with DOWNLOAD_LOG.open(
        "a",
        encoding="utf-8",
    ) as file:

        if first_write:

            file.write(
                "timestamp,"
                "symbol,"
                "timeframe,"
                "status,"
                "rows,"
                "error\n"
            )

        file.write(

            f"{datetime.now().isoformat()},"

            f"{symbol},"

            f"{timeframe.name},"

            f"{status},"

            f"{rows},"

            f"\"{error}\"\n"

        )


# ==========================================================
# DOWNLOAD ONE DATASET
# ==========================================================

def download_one(
    market,
    timeframe: Timeframe,
    job: int,
    total_jobs: int,
) -> None:

    symbol = market.symbol

    parquet_file = REPOSITORY.parquet_file(
        symbol,
        timeframe,
    )

    csv_file = (
        REPOSITORY.csv_file(
            symbol,
            timeframe,
        )
        if EXPORT_CSV
        else None
    )

    start_date = market.history_start(
        timeframe,
    )

    print()
    print("=" * 70)

    print(
        f"[{job}/{total_jobs}] "
        f"{symbol} | {timeframe.name}"
    )

    print("=" * 70)

    print(
        f"History : "
        f"{start_date} -> {END_DATE}"
    )

    if parquet_file.exists():

        print(
            "Already downloaded."
        )

        write_log(

            symbol=symbol,

            timeframe=timeframe,

            status="SKIPPED",

        )

        return

    manager = HistoryDownloadManager(

        symbol=symbol,

        timeframe=timeframe,

        batch_days=DOWNLOAD_BATCH_DAYS,

    )

    start_time = datetime.now()    
    try:

        manager.download_full(

            start=start_date,

            end=END_DATE,

            parquet_file=parquet_file,

            csv_file=csv_file,

        )

        elapsed = (
            datetime.now() - start_time
        )

        rows = 0

        try:

            import pandas as pd

            rows = len(
                pd.read_parquet(
                    parquet_file
                )
            )

        except Exception:

            pass

        print()
        print("SUCCESS")
        print(
            f"Rows    : {rows:,}"
        )
        print(
            f"Elapsed : {elapsed}"
        )
        print(
            f"Saved   : {parquet_file}"
        )

        write_log(

            symbol=symbol,

            timeframe=timeframe,

            status="SUCCESS",

            rows=rows,

        )

    except Exception as ex:

        print()
        print("FAILED")
        print(ex)

        write_log(

            symbol=symbol,

            timeframe=timeframe,

            status="FAILED",

            error=str(ex),

        )


# ==========================================================
# MAIN
# ==========================================================

def main() -> None:

    if DOWNLOAD_LOG.exists():

        DOWNLOAD_LOG.unlink()

    total_jobs = (

        len(MARKET_UNIVERSE)

        * len(TIMEFRAMES)

    )

    print("\n" + "=" * 70)
    print("NAKSHATRA ALPHA")
    print("COMPLETE MARKET DOWNLOAD")
    print("=" * 70)

    print(f"Markets    : {len(MARKET_UNIVERSE)}")
    print(f"Timeframes : {len(TIMEFRAMES)}")
    print(f"Jobs       : {total_jobs}")

    job = 1

    for timeframe in TIMEFRAMES:

        print("\n")
        print("=" * 70)

        print(
            f"DOWNLOADING : {timeframe.name}"
        )

        print("=" * 70)

        for market in MARKET_UNIVERSE:

            download_one(

                market=market,

                timeframe=timeframe,

                job=job,

                total_jobs=total_jobs,

            )

            job += 1

    print("\n")
    print("=" * 70)
    print("DOWNLOAD COMPLETED")
    print("=" * 70)

    print()

    print(
        f"Download Log : {DOWNLOAD_LOG}"
    )


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()