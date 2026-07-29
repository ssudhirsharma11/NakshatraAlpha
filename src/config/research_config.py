"""
Research Configuration

Central configuration used by research modules.
"""

from pathlib import Path

from src.models.location import Location

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

# ------------------------------------------------------------------
# Market Data
# ------------------------------------------------------------------

# Current research dataset.
# Replace this with a longer history file whenever required.
MARKET_DATA_FILE = (
    RAW_DATA_DIR /
    "256265_5minute_20260427_20260717.csv"
)

# ------------------------------------------------------------------
# Research Location
# ------------------------------------------------------------------

# All astrology calculations use this location unless
# explicitly overridden.

RESEARCH_LOCATION = Location(
    name="Jamshedpur",
    latitude=22.8046,
    longitude=86.2029,
    timezone="Asia/Kolkata",
)