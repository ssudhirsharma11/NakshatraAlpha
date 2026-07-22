"""
Tithi Reference Data

Contains immutable metadata for all 30 Tithis.
"""

from dataclasses import dataclass

from src.models.tithi_enum import Tithi


TITHI_SIZE = 12.0


@dataclass(frozen=True)
class TithiData:
    """
    Immutable metadata for one Tithi.
    """

    number: int
    tithi: Tithi
    paksha: str
    start_angle: float
    end_angle: float


TITHI_DATA = {}

for tithi in Tithi:

    number = tithi.value

    paksha = "Shukla" if number <= 15 else "Krishna"

    start = (number - 1) * TITHI_SIZE
    end = number * TITHI_SIZE

    TITHI_DATA[tithi] = TithiData(
        number=number,
        tithi=tithi,
        paksha=paksha,
        start_angle=start,
        end_angle=end,
    )