"""
Tithi Calculation
"""

from dataclasses import dataclass


@dataclass
class TithiInfo:
    name: str
    number: int
    paksha: str
    group: str
    lord: str


class Tithi:

    TITHI_NAMES = [
        "Pratipada",
        "Dwitiya",
        "Tritiya",
        "Chaturthi",
        "Panchami",
        "Shashthi",
        "Saptami",
        "Ashtami",
        "Navami",
        "Dashami",
        "Ekadashi",
        "Dwadashi",
        "Trayodashi",
        "Chaturdashi",
        "Purnima",
    ]

    GROUPS = {
        1: ("Nanda", "Venus"),
        2: ("Bhadra", "Mercury"),
        3: ("Jaya", "Mars"),
        4: ("Rikta", "Saturn"),
        5: ("Poorna", "Jupiter"),
        6: ("Nanda", "Venus"),
        7: ("Bhadra", "Mercury"),
        8: ("Jaya", "Mars"),
        9: ("Rikta", "Saturn"),
        10: ("Poorna", "Jupiter"),
        11: ("Nanda", "Venus"),
        12: ("Bhadra", "Mercury"),
        13: ("Jaya", "Mars"),
        14: ("Rikta", "Saturn"),
        15: ("Poorna", "Jupiter"),
    }

    @staticmethod
    def calculate(sun_longitude: float, moon_longitude: float):

        difference = (moon_longitude - sun_longitude) % 360

        tithi_number = int(difference / 12) + 1

        if tithi_number <= 15:
            paksha = "Shukla"
            name = Tithi.TITHI_NAMES[tithi_number - 1]
            lookup = tithi_number

        else:
            paksha = "Krishna"
            name = Tithi.TITHI_NAMES[tithi_number - 16]

            if tithi_number == 30:
                return TithiInfo(
                    "Amavasya",
                    30,
                    "Krishna",
                    "Research",
                    "Research Pending",
                )

            lookup = tithi_number - 15

        group, lord = Tithi.GROUPS[lookup]

        return TithiInfo(
            name,
            tithi_number,
            paksha,
            group,
            lord,
        )