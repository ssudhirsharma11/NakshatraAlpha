"""
Research Context

Carries everything required to generate
research features.
"""

from dataclasses import dataclass

from src.models.chart import Chart
from src.models.location import Location


@dataclass(frozen=True)
class ResearchContext:
    """
    Bundles the chart together with the
    original geographical location.
    """

    chart: Chart
    location: Location