"""
Tithi Position Model

Represents the calculated Tithi at a given timestamp.
"""

from dataclasses import dataclass

from src.models.paksha import Paksha
from src.models.planet import Planet
from src.models.tithi_enum import Tithi
from src.models.tithi_group import TithiGroup


@dataclass(frozen=True)
class TithiPosition:
    """
    Represents the current lunar Tithi together with
    all immutable metadata required for research.
    """

    # ---------------------------------------------------------
    # Basic Information
    # ---------------------------------------------------------

    tithi: Tithi

    number: int

    paksha: Paksha

    # ---------------------------------------------------------
    # Research Classification
    # ---------------------------------------------------------

    tithi_group: TithiGroup

    tithi_lord: Planet

    # ---------------------------------------------------------
    # Astronomical Information
    # ---------------------------------------------------------

    angular_distance: float

    degrees_in_tithi: float

    degrees_remaining: float

    progress: float

    # ---------------------------------------------------------
    # Convenience Properties
    # ---------------------------------------------------------

    @property
    def completed(self) -> bool:
        """
        Returns True if the Tithi is complete.
        """

        return self.progress >= 100.0

    @property
    def remaining_pct(self) -> float:
        """
        Remaining percentage of the current Tithi.
        """

        return 100.0 - self.progress