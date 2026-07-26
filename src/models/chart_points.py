"""
Chart Points Model

Represents all non-planetary points in a chart.

These are calculated independently of planetary positions and
can be progressively populated as new astrology modules are added.

Examples:
    - Lagna (Ascendant)
    - Midheaven (MC)
    - Vertex
    - Arudha Lagna
    - Hora Lagna
    - Ghati Lagna
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.lagna_position import LagnaPosition


@dataclass(frozen=True)
class ChartPoints:
    """
    Holds all non-planetary chart points.

    Every field is optional because different engines are implemented
    incrementally. As new modules are completed, additional fields can
    be populated without affecting existing code.
    """

    lagna: LagnaPosition | None = None

    # Future Extensions
    # -----------------
    # mc: MCPosition | None = None
    # vertex: VertexPosition | None = None
    # arudha_lagna: ArudhaLagnaPosition | None = None
    # hora_lagna: HoraLagnaPosition | None = None
    # ghati_lagna: GhatiLagnaPosition | None = None
    # bhava_lagna: BhavaLagnaPosition | None = None