"""
Sun Service

Responsible for sunrise, sunset and daylight calculations.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta

from core.defaults import DEFAULT_LOCATION


@dataclass
class SunInfo:

    sunrise: datetime
    sunset: datetime
    daylight_hours: float


class SunService:

    def get(self):

        # Placeholder values.
        # Sprint 18 will replace this with
        # Swiss Ephemeris sunrise/sunset.

        today = datetime.now()

        sunrise = today.replace(
            hour=5,
            minute=15,
            second=0,
            microsecond=0,
        )

        sunset = today.replace(
            hour=18,
            minute=25,
            second=0,
            microsecond=0,
        )

        daylight = (
            sunset - sunrise
        ) / timedelta(hours=1)

        return SunInfo(
            sunrise,
            sunset,
            daylight,
        )