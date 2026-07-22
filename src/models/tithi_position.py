"""
Tithi Position Model
"""

from dataclasses import dataclass

from src.models.tithi_enum import Tithi


@dataclass(frozen=True)
class TithiPosition:
    """
    Represents the current lunar tithi.
    """

    tithi: Tithi

    number: int

    paksha: str

    angular_distance: float

    degrees_in_tithi: float

    degrees_remaining: float