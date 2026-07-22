"""
Sign Information

Permanent knowledge of zodiac signs.
"""

from src.models.planet import Planet

SIGN_INFO = {

    "Aries": {
        "lord": Planet.MARS,
        "sector": [
            "Auto",
            "Pharma",
            "Infrastructure",
            "Capital Goods",
            "Hospital",
            "Healthcare",
            "Cement",
        ],
    },

    "Taurus": {
        "lord": Planet.VENUS,
        "sector": [
            "Banking",
            "Finance",
            "Media",
            "Sugar",
            "Hotel",
            "Cosmetics",
            "Perfumes",
            "Garments",
            "Diamonds",
            "Paint",
            "Insurance",
        ],
    },

    "Gemini": {
        "lord": Planet.MERCURY,
        "sector": [
            "Telecom",
            "Media",
            "Export",
            "Insurance",
            "Airline",
            "FMCG",
            "Banking",
            "IT",
            "Textile",
            "Mobile",
            "Newspaper",
        ],
    },

    "Cancer": {
        "lord": Planet.MOON,
        "sector": [
            "Water",
            "Oil & Gas",
            "Petrol",
            "Alcohol",
            "Rice",
            "Food Grain",
        ],
    },

    "Leo": {
        "lord": Planet.SUN,
        "sector": [
            "Power",
            "Media",
            "Gold",
            "Nuclear Energy",
            "Weapons",
        ],
    },

    "Virgo": {
        "lord": Planet.MERCURY,
        "sector": [
            "Telecom",
            "Media",
            "Mobile",
            "Insurance",
            "Animal Feed",
            "Fish Feed",
        ],
    },

    "Libra": {
        "lord": Planet.VENUS,
        "sector": [
            "Banking",
            "Finance",
            "Investment",
            "FMCG",
            "Paint",
            "Tourism",
            "Travel",
        ],
    },

    "Scorpio": {
        "lord": Planet.MARS,
        "sector": [
            "Auto",
            "Pharma",
            "Infrastructure",
            "Capital Goods",
            "Hospital",
            "Healthcare",
            "Cement",
        ],
    },

    "Sagittarius": {
        "lord": Planet.JUPITER,
        "sector": [
            "Insurance",
            "Banking",
            "Finance",
            "Export",
            "Wheat",
            "Food Grain",
        ],
    },

    "Capricorn": {
        "lord": Planet.SATURN,
        "sector": [
            "Leather",
            "Footwear",
            "Real Estate",
            "Pharma",
            "Steel",
            "Livestock",
            "Mining",
        ],
    },

    "Aquarius": {
        "lord": Planet.SATURN,
        "sector": [
            "Leather",
            "Footwear",
            "Real Estate",
            "Pharma",
            "Steel",
            "Livestock",
            "Mining",
        ],
    },

    "Pisces": {
        "lord": Planet.JUPITER,
        "sector": [
            "Food Grain",
            "Insurance",
            "Banking",
            "Finance",
            "Export",
        ],
    },

}