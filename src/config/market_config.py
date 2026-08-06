"""
Market Configuration

Central configuration for historical market data.

All market-related settings should be defined here so the
rest of the application does not hardcode symbols,
intervals, paths or download dates.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from src.market.timeframe import Timeframe


# ==========================================================
# Instrument
# ==========================================================

DEFAULT_SYMBOL = "NIFTY 50"

# Future expansion
#
# BANKNIFTY
# FINNIFTY
# MIDCPNIFTY
#

# ==========================================================
# Timeframe
# ==========================================================

DEFAULT_TIMEFRAME = Timeframe.MINUTE_5

# ==========================================================
# Historical Download
# ==========================================================

# Earliest date we want to maintain locally.
#
# Change only if we decide to rebuild history further back.

HISTORY_START_DATE = date(
    2000,
    1,
    1,
)
INTRADAY_HISTORY_START = date(
    2015,
    1,
    1,
)
# ==========================================================
# Storage
# ==========================================================

MARKET_DATA_DIR = Path(
    "data/market"
)

MARKET_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def get_timeframe_name(
    timeframe: Timeframe,
) -> str:
    """
    Returns a filename-friendly timeframe.
    """

    mapping = {

        Timeframe.MINUTE_1: "1minute",

        Timeframe.MINUTE_5: "5minute",

        Timeframe.MINUTE_15: "15minute",

        Timeframe.MINUTE_30: "30minute",

        Timeframe.HOUR_1: "60minute",

        Timeframe.DAILY: "daily",

        Timeframe.WEEKLY: "weekly",

    }

    return mapping[timeframe]


def get_parquet_file(
    symbol: str,
    timeframe: Timeframe,
) -> Path:
    """
    Returns parquet filename for any instrument.
    """

    symbol = (
        symbol
        .lower()
        .replace(" ", "_")
    )

    return (
        MARKET_DATA_DIR /
        f"{symbol}_{get_timeframe_name(timeframe)}.parquet"
    )


def get_csv_file(
    symbol: str,
    timeframe: Timeframe,
) -> Path:
    """
    Returns csv filename for any instrument.
    """

    symbol = (
        symbol
        .lower()
        .replace(" ", "_")
    )

    return (
        MARKET_DATA_DIR /
        f"{symbol}_{get_timeframe_name(timeframe)}.csv"
    )
# ==========================================================
# Download Behaviour
# ==========================================================

# Number of calendar days per download request.
#
# Keep comfortably below Kite API limits.
#
# Can be tuned later after testing.

DOWNLOAD_BATCH_DAYS = 90

# Save CSV in addition to Parquet.
#
# Parquet remains the master file.

EXPORT_CSV = False

# ==========================================================
# Validation
# ==========================================================

REMOVE_DUPLICATES = True

SORT_BY_TIMESTAMP = True

VALIDATE_AFTER_DOWNLOAD = True