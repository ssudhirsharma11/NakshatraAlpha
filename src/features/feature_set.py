"""
Research Feature Set

Represents all astrology-derived features
for one timestamp.
"""

from dataclasses import dataclass

from src.models.chart import Chart


@dataclass(frozen=True)
class FeatureSet:
    """
    Engineered features derived from an astronomical Chart.

    The Chart contains raw astronomical facts.
    FeatureSet contains derived research features used for
    backtesting and statistical analysis.
    """

    # ---------------------------------------------------------
    # Source Chart
    # ---------------------------------------------------------

    chart: Chart

    # ---------------------------------------------------------
    # Nakshatra Features
    # ---------------------------------------------------------

    moon_nakshatra: str
    moon_nakshatra_number: int

    sun_nakshatra: str
    sun_nakshatra_number: int

    # ---------------------------------------------------------
    # Lunar Calendar Features
    # ---------------------------------------------------------

    tithi: str
    tithi_number: int

    paksha: str

    # ---------------------------------------------------------
    # Planet Relationship Features
    # ---------------------------------------------------------

    saturn_from_sun: int

    saturn_kendra_from_sun: bool