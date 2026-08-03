"""
Tithi Reference Data

Contains immutable metadata for all 30 Tithis.
"""

from dataclasses import dataclass

from src.models.paksha import Paksha
from src.models.planet import Planet
from src.models.tithi_enum import Tithi
from src.models.tithi_group import TithiGroup


TITHI_SIZE = 12.0


@dataclass(frozen=True)
class TithiData:
    """
    Immutable metadata for one Tithi.
    """

    number: int
    tithi: Tithi
    paksha: Paksha

    tithi_group: TithiGroup
    tithi_lord: Planet

    start_angle: float
    end_angle: float


# ---------------------------------------------------------
# Research Mapping
# ---------------------------------------------------------

GROUP_SEQUENCE = (
    (TithiGroup.NANDA, Planet.VENUS),
    (TithiGroup.BHADRA, Planet.MERCURY),
    (TithiGroup.JAYA, Planet.MARS),
    (TithiGroup.RIKTA, Planet.SATURN),
    (TithiGroup.POORNA, Planet.JUPITER),
)


TITHI_DATA: dict[Tithi, TithiData] = {}

for tithi in Tithi:

    number = tithi.value

    paksha = (
        Paksha.SHUKLA
        if number <= 15
        else Paksha.KRISHNA
    )

    start = (number - 1) * TITHI_SIZE
    end = number * TITHI_SIZE

    group, lord = GROUP_SEQUENCE[
        (number - 1) % 5
    ]

    TITHI_DATA[tithi] = TithiData(
        number=number,
        tithi=tithi,
        paksha=paksha,

        tithi_group=group,
        tithi_lord=lord,

        start_angle=start,
        end_angle=end,
    )