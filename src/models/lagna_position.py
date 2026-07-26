"""
Lagna Position Model

Represents the Ascendant (Lagna) position in the zodiac.
"""

from dataclasses import dataclass

from src.models.sign import Sign


@dataclass(frozen=True)
class LagnaPosition:
    """
    Immutable representation of the Ascendant.
    """

    longitude: float

    rashi: Sign
    rashi_number: int
    degrees_in_rashi: float

    @property
    def formatted(self) -> str:
        """
        Human-readable representation.

        Example:
            Aries 12.3456°
        """
        return (
            f"{self.rashi.name} "
            f"{self.degrees_in_rashi:.4f}°"
        )