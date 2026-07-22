"""
Nakshatra Enumeration

Defines the 27 Nakshatras in their traditional order.
"""

from enum import Enum


class Nakshatra(Enum):

    ASHWINI = 1
    BHARANI = 2
    KRITTIKA = 3
    ROHINI = 4
    MRIGASHIRA = 5
    ARDRA = 6
    PUNARVASU = 7
    PUSHYA = 8
    ASHLESHA = 9

    MAGHA = 10
    PURVA_PHALGUNI = 11
    UTTARA_PHALGUNI = 12
    HASTA = 13
    CHITRA = 14
    SWATI = 15
    VISHAKHA = 16
    ANURADHA = 17
    JYESHTHA = 18

    MULA = 19
    PURVA_ASHADHA = 20
    UTTARA_ASHADHA = 21
    SHRAVANA = 22
    DHANISHTA = 23
    SHATABHISHA = 24
    PURVA_BHADRAPADA = 25
    UTTARA_BHADRAPADA = 26
    REVATI = 27