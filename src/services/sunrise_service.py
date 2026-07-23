from __future__ import annotations

from datetime import date

from src.models.location import Location
from src.models.sun_times import SunTimes


class SunriseService:
    """
    Calculates sunrise and sunset for a given date
    and location.

    Implementation will use Swiss Ephemeris.
    """

    @staticmethod
    def calculate(
        calculation_date: date,
        location: Location,
    ) -> SunTimes:
        """
        Returns SunTimes for the supplied date.

        NOTE:
        Swiss Ephemeris implementation will be added
        in the next milestone.
        """
        raise NotImplementedError(
            "Swiss Ephemeris sunrise calculation not implemented yet."
        )