"""
Zodiac (Rashi) calculations.

Provides reusable zodiac calculations independent of
Navamsha or any divisional chart.
"""

from src.models.sign import Sign


class ZodiacEngine:
    """
    Stateless zodiac calculation engine.

    Kept for backward compatibility with existing tests
    and future service usage.
    """

    @staticmethod
    def normalize_longitude(longitude: float) -> float:
        return longitude % 360.0

    @staticmethod
    def sign_index(longitude: float) -> int:
        return int(ZodiacEngine.normalize_longitude(longitude) // 30)

    @staticmethod
    def sign(longitude: float) -> Sign:
        return Sign(ZodiacEngine.sign_index(longitude) + 1)

    @staticmethod
    def degrees_in_sign(longitude: float) -> float:
        return ZodiacEngine.normalize_longitude(longitude) % 30.0

    @staticmethod
    def zodiac_details(longitude: float) -> dict:
        rashi = ZodiacEngine.sign(longitude)

        return {
            "rashi": rashi,
            "rashi_number": rashi.value,
            "degrees_in_rashi": ZodiacEngine.degrees_in_sign(longitude),
        }


# ------------------------------------------------------------------
# Backward-compatible function wrappers
# ------------------------------------------------------------------

def normalize_longitude(longitude: float) -> float:
    return ZodiacEngine.normalize_longitude(longitude)


def sign_index(longitude: float) -> int:
    return ZodiacEngine.sign_index(longitude)


def sign(longitude: float) -> Sign:
    return ZodiacEngine.sign(longitude)


def degrees_in_sign(longitude: float) -> float:
    return ZodiacEngine.degrees_in_sign(longitude)


def zodiac_details(longitude: float) -> dict:
    return ZodiacEngine.zodiac_details(longitude)