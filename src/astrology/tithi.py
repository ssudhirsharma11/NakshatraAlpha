"""
Tithi Calculation

Calculates live Tithi from Sun and Moon longitudes.
"""

from dataclasses import dataclass

from services.ephemeris_service import EphemerisService


@dataclass
class Tithi:

    name: str
    paksha: str
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

    GROUPS = [
        "Nanda",
        "Bhadra",
        "Jaya",
        "Rikta",
        "Poorna",
    ]

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

        difference = moon - sun

        if difference < 0:
            difference += 360.0

        # 1 to 30
        tithi_number = int(difference / 12.0) + 1

        if tithi_number > 30:
            tithi_number = 30

        name = self.TITHI_NAMES[tithi_number - 1]

        if tithi_number <= 15:
            paksha = "Shukla"
        else:
            paksha = "Krishna"

        # Amavasya handled separately
        if tithi_number == 30:
            group = "Research"
            lord = "Research Pending"
        else:
            group = self.GROUPS[(tithi_number - 1) % 5]
            lord = self.LORDS[group]

        return Tithi(
            name=name,
            paksha=paksha,
            group=group,
            lord=lord,
        )