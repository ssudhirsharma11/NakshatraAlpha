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

DEFAULT_SYMBOL = "NIFTY"

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
    2021,
    7,
    24,
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

PARQUET_FILE = (
    MARKET_DATA_DIR /
    "nifty_5min.parquet"
)

CSV_FILE = (
    MARKET_DATA_DIR /
    "nifty_5min.csv"
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