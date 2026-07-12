"""
Zodiac Sign Engine
"""


class Zodiac:

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

    @staticmethod
    def sign(longitude: float):

        index = int(longitude // 30)

        return Zodiac.SIGNS[index]