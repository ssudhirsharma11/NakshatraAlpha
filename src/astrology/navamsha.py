"""
Navamsha (D9) calculations.

Swiss Ephemeris returns sidereal longitude.
This module converts a longitude into:

- Rashi
- Degrees within Rashi
- Navamsha
- Navamsha Lord
"""

from src.models.sign import Sign


def normalize_longitude(longitude: float) -> float:
    return longitude % 360.0


def sign_index(longitude: float) -> int:
    return int(normalize_longitude(longitude) // 30)


def sign(longitude: float) -> Sign:
    return Sign.from_index(sign_index(longitude))


def degrees_in_sign(longitude: float) -> float:
    return normalize_longitude(longitude) % 30.0


def navamsha_number(longitude: float) -> int:
    deg = degrees_in_sign(longitude)
    return int(deg // (30 / 9)) + 1


def navamsha_sign(longitude: float) -> Sign:

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

    return Sign.from_index((start + nav_no) % 12)


def navamsha_lord(longitude: float):
    return navamsha_sign(longitude).lord


def navamsha_details(longitude: float) -> dict:

    rashi = sign(longitude)
    navamsha = navamsha_sign(longitude)

    return {
        "rashi": rashi,
        "rashi_number": rashi.number,
        "degrees_in_rashi": degrees_in_sign(longitude),
        "navamsha": navamsha,
        "navamsha_number": navamsha_number(longitude),
        "navamsha_lord": navamsha.lord,
    }