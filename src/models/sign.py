"""
Zodiac Sign Enum
"""

from enum import Enum

from src.models.planet import Planet


class Sign(Enum):
    ARIES = ("Aries", Planet.MARS)
    TAURUS = ("Taurus", Planet.VENUS)
    GEMINI = ("Gemini", Planet.MERCURY)
    CANCER = ("Cancer", Planet.MOON)
    LEO = ("Leo", Planet.SUN)
    VIRGO = ("Virgo", Planet.MERCURY)
    LIBRA = ("Libra", Planet.VENUS)
    SCORPIO = ("Scorpio", Planet.MARS)
    SAGITTARIUS = ("Sagittarius", Planet.JUPITER)
    CAPRICORN = ("Capricorn", Planet.SATURN)
    AQUARIUS = ("Aquarius", Planet.SATURN)
    PISCES = ("Pisces", Planet.JUPITER)

    def __init__(self, label: str, lord: Planet):
        self.label = label
        self.lord = lord

    @staticmethod
    def from_index(index: int) -> "Sign":
        """
        Returns the sign for a zero-based index.

        0 = Aries
        1 = Taurus
        ...
        11 = Pisces
        """
        return tuple(Sign)[index % 12]

    @staticmethod
    def from_name(name: str) -> "Sign":
        """
        Returns the Sign enum from its display name.
        """
        for sign in Sign:
            if sign.label == name:
                return sign

        raise ValueError(f"Unknown sign: {name}")

    @staticmethod
    def from_longitude(longitude: float) -> "Sign":
        """
        Returns the zodiac sign for an ecliptic longitude.
        """
        longitude = longitude % 360.0
        index = int(longitude // 30.0)
        return Sign.from_index(index)

    @staticmethod
    def degrees_in_sign(longitude: float) -> float:
        """
        Returns the longitude within the current sign.

        Example:
            37.5° -> 7.5°
            295°  -> 25°
        """
        return longitude % 30.0

    @property
    def number(self) -> int:
        """
        Aries = 1
        Taurus = 2
        ...
        Pisces = 12
        """
        return tuple(Sign).index(self) + 1

    def __str__(self):
        return self.label