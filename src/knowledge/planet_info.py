"""
Planet Information

Permanent knowledge of planets.

This file stores static information only.
No calculations should be written here.
"""

from models.planet import Planet


PLANET_INFO = {

    Planet.SUN: {
        "rules": ["Leo"],
        "sector": [
            "Power",
            "Media",
            "Nuclear Energy",
            "PSU",
            "Nifty",
            "Firearms",
        ],
        "metal": [
            "Gold",
            "Copper",
            "Bronze",
        ],
        "remarks": "",
    },

    Planet.MOON: {
        "rules": ["Cancer"],
        "sector": [
            "Petroleum",
            "Shipping",
            "Oil & Gas",
            "Bank Nifty",
            "Soft Drinks",
            "Water",
            "Milk",
            "Crude",
            "Alcohol",
        ],
        "metal": [],
        "remarks": "Feels weak in Capricorn",
    },

    Planet.MARS: {
        "rules": ["Aries", "Scorpio"],
        "sector": [
            "Healthcare",
            "Capital Goods",
            "Auto",
            "Pharma",
            "Cement",
            "Infrastructure",
            "Steel",
            "Metal",
            "Crude",
            "Firearms",
            "Tobacco",
            "Real Estate",
        ],
        "metal": [],
        "remarks": "",
    },

    Planet.MERCURY: {
        "rules": ["Gemini", "Virgo"],
        "sector": [
            "Media",
            "Communication",
            "FMCG",
            "IT",
            "Textile",
            "Banking",
            "Insurance",
            "Aviation",
            "Agro",
            "Food Grain",
            "Newspaper",
        ],
        "metal": [],
        "remarks": "Feels weak with Mars",
    },

    Planet.JUPITER: {
        "rules": ["Sagittarius", "Pisces"],
        "sector": [
            "Banking",
            "Gems",
            "Edible Oil",
            "Gold",
            "Exports",
        ],
        "metal": [],
        "remarks": "Jupiter orders. Sun and Mars follow.",
    },

    Planet.VENUS: {
        "rules": ["Taurus", "Libra"],
        "sector": [
            "Diamond",
            "Auto",
            "Hospitality",
            "Gems",
            "Jewellery",
            "Garments",
        ],
        "metal": [],
        "remarks": "",
    },

    Planet.SATURN: {
        "rules": ["Capricorn", "Aquarius"],
        "sector": [
            "Entire Market",
            "Cement",
            "Infrastructure",
            "Steel",
            "Footwear",
            "Crude",
            "Mining",
            "Gas",
            "Coal",
        ],
        "metal": [],
        "remarks": (
            "Most important market planet. "
            "Research: 2028–2030 may represent a bear phase."
        ),
    },

    Planet.RAHU: {
        "rules": ["Aquarius"],
        "sector": [
            "Media",
            "Power",
            "Telecom",
            "Communication",
            "Electrical Goods",
            "Infrastructure",
            "Cement",
            "Metal",
        ],
        "metal": [],
        "remarks": "",
    },

    Planet.KETU: {
        "rules": ["Scorpio"],
        "sector": [
            "Power",
            "IT",
            "Watches",
            "Crude",
            "Iron",
            "Steel",
        ],
        "metal": [],
        "remarks": "",
    },
}