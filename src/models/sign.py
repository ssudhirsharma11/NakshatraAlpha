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
        signs = list(Sign)
        return signs[index % 12]

    @staticmethod
    def from_name(name: str) -> "Sign":
        for sign in Sign:
            if sign.label == name:
                return sign
        raise ValueError(f"Unknown sign: {name}")

    @property
    def number(self) -> int:
        return list(Sign).index(self) + 1

    def __str__(self):
        return self.label