from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ResearchRow:
    """
    One research observation.

    One row represents one market candle
    (currently 1 Hour).

    This object combines:

    - Market data
    - Astrological features
    - Research-only features

    It should NEVER contain analysis,
    signals or opinions.
    """

    # ======================================================
    # Dataset Metadata
    # ======================================================

    dataset_version: int
    research_id: str

    # ======================================================
    # Candle
    # ======================================================

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float

    # ======================================================
    # Derived Market Statistics
    # ======================================================

    return_pct: float
    range_pct: float

    # ======================================================
    # Panchang
    # ======================================================

    hora: str

    tithi: str
    tithi_number: int

    paksha: str

    # ======================================================
    # Lagna
    # ======================================================

    lagna: str

    navamsha_lagna: str

    # ======================================================
    # Planet Positions
    # ======================================================

    sun_rashi: str
    moon_rashi: str
    mars_rashi: str
    mercury_rashi: str
    venus_rashi: str
    jupiter_rashi: str
    saturn_rashi: str
    rahu_rashi: str
    ketu_rashi: str

    # ======================================================
    # Navamsha
    # ======================================================

    sun_navamsha: str
    moon_navamsha: str
    mars_navamsha: str
    mercury_navamsha: str
    venus_navamsha: str
    jupiter_navamsha: str
    saturn_navamsha: str
    rahu_navamsha: str
    ketu_navamsha: str

    # ======================================================
    # Nakshatra
    # ======================================================

    moon_nakshatra: str

    # ======================================================
    # Research Features
    # ======================================================

    saturn_from_sun: int

    saturn_kendra_from_sun: bool

    sadesati: bool