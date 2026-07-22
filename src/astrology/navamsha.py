"""
Navamsha (D9) calculations.

Swiss Ephemeris returns tropical/sidereal longitude.
This module converts a longitude into:

- Rashi
- Degrees within rashi
- Navamsha number (1-9)
- Navamsha sign
- Navamsha lord
"""

from src.knowledge.sign_info import SIGN_INFO

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


def normalize_longitude(longitude: float) -> float:
    """Normalize longitude to 0 <= x < 360."""
    return longitude % 360.0


def sign_index(longitude: float) -> int:
    """0=Aries ... 11=Pisces"""
    return int(normalize_longitude(longitude) // 30)


def sign_name(longitude: float) -> str:
    return SIGNS[sign_index(longitude)]


def degrees_in_sign(longitude: float) -> float:
    return normalize_longitude(longitude) % 30.0


def navamsha_number(longitude: float) -> int:
    """
    Returns Navamsha number (1-9)
    """
    deg = degrees_in_sign(longitude)
    return int(deg // (30 / 9)) + 1


def navamsha_sign(longitude: float) -> str:
    """
    Calculate D9 sign.

    Rules:

    Movable signs:
        Aries Cancer Libra Capricorn
        -> start from same sign

    Fixed signs:
        Taurus Leo Scorpio Aquarius
        -> start from 9th sign

    Dual signs:
        Gemini Virgo Sagittarius Pisces
        -> start from 5th sign
    """

    rashi = sign_index(longitude)
    nav_no = navamsha_number(longitude) - 1

    # Movable
    if rashi in (0, 3, 6, 9):
        start = rashi

    # Fixed
    elif rashi in (1, 4, 7, 10):
        start = (rashi + 8) % 12

    # Dual
    else:
        start = (rashi + 4) % 12

    return SIGNS[(start + nav_no) % 12]


def navamsha_lord(longitude: float):
    """Returns planet enum from knowledge.sign_info"""
    return SIGN_INFO[navamsha_sign(longitude)]["lord"]


def navamsha_details(longitude: float) -> dict:
    """
    Convenience method.

    Returns everything required by ChartBuilder.
    """

    return {
        "rashi": sign_name(longitude),
        "rashi_number": sign_index(longitude) + 1,
        "degrees_in_rashi": degrees_in_sign(longitude),
        "navamsha_number": navamsha_number(longitude),
        "navamsha": navamsha_sign(longitude),
        "navamsha_lord": navamsha_lord(longitude),
    }