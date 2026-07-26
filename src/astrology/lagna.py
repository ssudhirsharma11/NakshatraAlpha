"""
Lagna Engine

Calculates the Ascendant (Lagna) for a given
date, time and location.
"""

from src.models.lagna_position import LagnaPosition
from src.models.sign import Sign
from src.services.ephemeris_service import EphemerisService


class LagnaEngine:
    """
    Calculates the sidereal Ascendant.
    """

    _ephemeris = EphemerisService()

    @classmethod
    def calculate(
        cls,
        timestamp,
        latitude: float,
        longitude: float,
    ) -> LagnaPosition:

        asc_longitude = cls._ephemeris.get_ascendant(
            timestamp,
            latitude,
            longitude,
        )

        sign = Sign.from_longitude(asc_longitude)

        return LagnaPosition(
            longitude=asc_longitude,
            rashi=sign,
            rashi_number=sign.number,
            degrees_in_rashi=Sign.degrees_in_sign(
                asc_longitude
            ),
        )