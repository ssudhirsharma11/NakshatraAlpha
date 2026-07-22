"""
Nakshatra Reference Data

Contains immutable metadata for all 27 Nakshatras.
"""

from dataclasses import dataclass

from src.models.nakshatra_enum import Nakshatra
from src.models.planet import Planet


NAKSHATRA_SIZE = 360.0 / 27.0
PADA_SIZE = NAKSHATRA_SIZE / 4.0


@dataclass(frozen=True)
class NakshatraData:
    """
    Immutable metadata for one Nakshatra.
    """

    number: int
    nakshatra: Nakshatra
    lord: Planet
    start_degree: float
    end_degree: float


NAKSHATRA_DATA = {

    Nakshatra.ASHWINI: NakshatraData(
        1, Nakshatra.ASHWINI, Planet.KETU,
        0.0, NAKSHATRA_SIZE
    ),

    Nakshatra.BHARANI: NakshatraData(
        2, Nakshatra.BHARANI, Planet.VENUS,
        NAKSHATRA_SIZE * 1,
        NAKSHATRA_SIZE * 2
    ),

    Nakshatra.KRITTIKA: NakshatraData(
        3, Nakshatra.KRITTIKA, Planet.SUN,
        NAKSHATRA_SIZE * 2,
        NAKSHATRA_SIZE * 3
    ),

    Nakshatra.ROHINI: NakshatraData(
        4, Nakshatra.ROHINI, Planet.MOON,
        NAKSHATRA_SIZE * 3,
        NAKSHATRA_SIZE * 4
    ),

    Nakshatra.MRIGASHIRA: NakshatraData(
        5, Nakshatra.MRIGASHIRA, Planet.MARS,
        NAKSHATRA_SIZE * 4,
        NAKSHATRA_SIZE * 5
    ),

    Nakshatra.ARDRA: NakshatraData(
        6, Nakshatra.ARDRA, Planet.RAHU,
        NAKSHATRA_SIZE * 5,
        NAKSHATRA_SIZE * 6
    ),

    Nakshatra.PUNARVASU: NakshatraData(
        7, Nakshatra.PUNARVASU, Planet.JUPITER,
        NAKSHATRA_SIZE * 6,
        NAKSHATRA_SIZE * 7
    ),

    Nakshatra.PUSHYA: NakshatraData(
        8, Nakshatra.PUSHYA, Planet.SATURN,
        NAKSHATRA_SIZE * 7,
        NAKSHATRA_SIZE * 8
    ),

    Nakshatra.ASHLESHA: NakshatraData(
        9, Nakshatra.ASHLESHA, Planet.MERCURY,
        NAKSHATRA_SIZE * 8,
        NAKSHATRA_SIZE * 9
    ),

    Nakshatra.MAGHA: NakshatraData(
        10, Nakshatra.MAGHA, Planet.KETU,
        NAKSHATRA_SIZE * 9,
        NAKSHATRA_SIZE * 10
    ),

    Nakshatra.PURVA_PHALGUNI: NakshatraData(
        11, Nakshatra.PURVA_PHALGUNI, Planet.VENUS,
        NAKSHATRA_SIZE * 10,
        NAKSHATRA_SIZE * 11
    ),

    Nakshatra.UTTARA_PHALGUNI: NakshatraData(
        12, Nakshatra.UTTARA_PHALGUNI, Planet.SUN,
        NAKSHATRA_SIZE * 11,
        NAKSHATRA_SIZE * 12
    ),

    Nakshatra.HASTA: NakshatraData(
        13, Nakshatra.HASTA, Planet.MOON,
        NAKSHATRA_SIZE * 12,
        NAKSHATRA_SIZE * 13
    ),

    Nakshatra.CHITRA: NakshatraData(
        14, Nakshatra.CHITRA, Planet.MARS,
        NAKSHATRA_SIZE * 13,
        NAKSHATRA_SIZE * 14
    ),

    Nakshatra.SWATI: NakshatraData(
        15, Nakshatra.SWATI, Planet.RAHU,
        NAKSHATRA_SIZE * 14,
        NAKSHATRA_SIZE * 15
    ),

    Nakshatra.VISHAKHA: NakshatraData(
        16, Nakshatra.VISHAKHA, Planet.JUPITER,
        NAKSHATRA_SIZE * 15,
        NAKSHATRA_SIZE * 16
    ),

    Nakshatra.ANURADHA: NakshatraData(
        17, Nakshatra.ANURADHA, Planet.SATURN,
        NAKSHATRA_SIZE * 16,
        NAKSHATRA_SIZE * 17
    ),

    Nakshatra.JYESHTHA: NakshatraData(
        18, Nakshatra.JYESHTHA, Planet.MERCURY,
        NAKSHATRA_SIZE * 17,
        NAKSHATRA_SIZE * 18
    ),

    Nakshatra.MULA: NakshatraData(
        19, Nakshatra.MULA, Planet.KETU,
        NAKSHATRA_SIZE * 18,
        NAKSHATRA_SIZE * 19
    ),

    Nakshatra.PURVA_ASHADHA: NakshatraData(
        20, Nakshatra.PURVA_ASHADHA, Planet.VENUS,
        NAKSHATRA_SIZE * 19,
        NAKSHATRA_SIZE * 20
    ),

    Nakshatra.UTTARA_ASHADHA: NakshatraData(
        21, Nakshatra.UTTARA_ASHADHA, Planet.SUN,
        NAKSHATRA_SIZE * 20,
        NAKSHATRA_SIZE * 21
    ),

    Nakshatra.SHRAVANA: NakshatraData(
        22, Nakshatra.SHRAVANA, Planet.MOON,
        NAKSHATRA_SIZE * 21,
        NAKSHATRA_SIZE * 22
    ),

    Nakshatra.DHANISHTA: NakshatraData(
        23, Nakshatra.DHANISHTA, Planet.MARS,
        NAKSHATRA_SIZE * 22,
        NAKSHATRA_SIZE * 23
    ),

    Nakshatra.SHATABHISHA: NakshatraData(
        24, Nakshatra.SHATABHISHA, Planet.RAHU,
        NAKSHATRA_SIZE * 23,
        NAKSHATRA_SIZE * 24
    ),

    Nakshatra.PURVA_BHADRAPADA: NakshatraData(
        25, Nakshatra.PURVA_BHADRAPADA, Planet.JUPITER,
        NAKSHATRA_SIZE * 24,
        NAKSHATRA_SIZE * 25
    ),

    Nakshatra.UTTARA_BHADRAPADA: NakshatraData(
        26, Nakshatra.UTTARA_BHADRAPADA, Planet.SATURN,
        NAKSHATRA_SIZE * 25,
        NAKSHATRA_SIZE * 26
    ),

    Nakshatra.REVATI: NakshatraData(
        27, Nakshatra.REVATI, Planet.MERCURY,
        NAKSHATRA_SIZE * 26,
        360.0
    ),
}