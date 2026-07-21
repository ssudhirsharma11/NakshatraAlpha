"""
Zodiac Engine

Converts a celestial longitude (0°–360°)
into Zodiac Sign information.
"""

from dataclasses import dataclass


@dataclass
class ZodiacSign:
    sign_number: int
    sign_name: str
    degree_in_sign: float


SIGNS = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]


class ZodiacEngine:

    @staticmethod
    def get_sign(longitude: float) -> ZodiacSign:
        """
        Parameters
        ----------
        longitude : float
            Planet longitude between 0° and <360°

        Returns
        -------
        ZodiacSign
        """

        longitude = longitude % 360

        sign_number = int(longitude // 30)

        degree_in_sign = longitude % 30

        return ZodiacSign(
            sign_number=sign_number + 1,
            sign_name=SIGNS[sign_number],
            degree_in_sign=round(degree_in_sign, 4),
        )