"""
Tithi Calculation

Calculates live Tithi from Sun and Moon longitudes.
"""

from dataclasses import dataclass

from services.ephemeris_service import EphemerisService


@dataclass
class Tithi:

    number: int
    name: str
    paksha: str
    phase: str
    illumination: float
    group: str
    lord: str


class TithiCalculator:

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
        "Amavasya",
    ]

    GROUPS = {
        1: "Nanda",
        2: "Bhadra",
        3: "Jaya",
        4: "Rikta",
        5: "Poorna",
    }

    LORDS = {
        "Nanda": "Venus",
        "Bhadra": "Mercury",
        "Jaya": "Mars",
        "Rikta": "Saturn",
        "Poorna": "Jupiter",
    }

    def get(self):

        ephemeris = EphemerisService()

        sun = ephemeris.current_sun_longitude()
        moon = ephemeris.current_moon_longitude()

        difference = (moon - sun) % 360.0

        tithi_number = int(difference // 12.0) + 1

        tithi_name = self.TITHI_NAMES[tithi_number - 1]

        if tithi_number <= 15:
            paksha = "Shukla"
            phase = "Waxing"
        else:
            paksha = "Krishna"
            phase = "Waning"

        illumination = 100 - abs(180 - difference) / 180 * 100

        remainder = tithi_number % 5

        if remainder == 1:
            group = "Nanda"
        elif remainder == 2:
            group = "Bhadra"
        elif remainder == 3:
            group = "Jaya"
        elif remainder == 4:
            group = "Rikta"
        else:
            group = "Poorna"

        if tithi_name == "Amavasya":
            lord = "Research Pending"
        else:
            lord = self.LORDS[group]

        return Tithi(
            number=tithi_number,
            name=tithi_name,
            paksha=paksha,
            phase=phase,
            illumination=round(illumination, 1),
            group=group,
            lord=lord,
        )