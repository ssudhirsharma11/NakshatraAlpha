"""
Lagna Position Model
"""

from __future__ import annotations

from dataclasses import dataclass

from src.models.zodiac import ZodiacSign


@dataclass(frozen=True)
class LagnaPosition:
    """
    Represents the Ascendant (Lagna).
    """

    longitude: float
    sign: ZodiacSign
    degree_in_sign: float

    @property
    def sign_number(self) -> int:
        return self.sign.value

    @property
    def formatted(self) -> str:
        return (
            f"{self.sign.name} "
            f"{self.degree_in_sign:.4f}°"
        )