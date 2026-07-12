"""
Nakshatra Utilities

Converts planetary longitude into one of the
27 Vedic Nakshatras.
"""


class Nakshatra:

    NAKSHATRAS = [
        "Ashwini",
        "Bharani",
        "Krittika",
        "Rohini",
        "Mrigashira",
        "Ardra",
        "Punarvasu",
        "Pushya",
        "Ashlesha",
        "Magha",
        "Purva Phalguni",
        "Uttara Phalguni",
        "Hasta",
        "Chitra",
        "Swati",
        "Vishakha",
        "Anuradha",
        "Jyeshtha",
        "Moola",
        "Purva Ashadha",
        "Uttara Ashadha",
        "Shravana",
        "Dhanishta",
        "Shatabhisha",
        "Purva Bhadrapada",
        "Uttara Bhadrapada",
        "Revati",
    ]

    @staticmethod
    def get(longitude: float):

        index = int(longitude / (360 / 27))

        return Nakshatra.NAKSHATRAS[index]