"""
Research Report Row

Represents one complete research observation.

One row corresponds to one market session within a Hora.
"""

from dataclasses import dataclass
from datetime import datetime

from src.models.chart import Chart
from src.models.feature_set import FeatureSet
from src.models.hora import Hora
from src.models.market_features import MarketFeatures
from src.models.market_snapshot import MarketSnapshot


@dataclass(slots=True)
class ResearchReportRow:
    """
    One row of the research report.
    """

    # ---------------------------------------------------------
    # Hora
    # ---------------------------------------------------------

    hora: Hora

    # ---------------------------------------------------------
    # Actual market interval used
    # ---------------------------------------------------------

    market_start: datetime

    market_end: datetime

    # ---------------------------------------------------------
    # Astrology
    # ---------------------------------------------------------

    chart: Chart

    features: FeatureSet

    # ---------------------------------------------------------
    # Market
    # ---------------------------------------------------------

    market: MarketSnapshot

    market_features: MarketFeatures