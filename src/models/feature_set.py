"""
Feature Set Model

Represents all derived research features generated
from a Chart.
"""

from dataclasses import dataclass

from src.models.chart import Chart


@dataclass(frozen=True)
class FeatureSet:
    """
    Holds all derived features used for quantitative
    astrology research.

    The Chart remains the source of astronomical truth.
    This class stores only engineered features.
    """

    chart: Chart

    # ----------------------------
    # Planet Relationships
    # ----------------------------

    saturn_from_sun: int
    saturn_kendra_from_sun: bool