"""
Sun Service

Responsible for sunrise, sunset and daylight calculations.
"""

from dataclasses import dataclass
from datetime import datetime

from astral import LocationInfo
from astral.sun import sun
from zoneinfo import ZoneInfo

from core.defaults import DEFAULT_LOCATION


@dataclass
class SunInfo:
    sunrise: datetime
    sunset: datetime
    daylight_hours: float


class SunService:

    def get(self):

        location = LocationInfo(
            DEFAULT_LOCATION.city,
            "India",
            DEFAULT_LOCATION.timezone,
            DEFAULT_LOCATION.latitude,
            DEFAULT_LOCATION.longitude,
        )

        tz = ZoneInfo(DEFAULT_LOCATION.timezone)

        s = sun(
            observer=location.observer,
            date=datetime.now(tz).date(),
            tzinfo=tz,
        )

        sunrise = s["sunrise"]
        sunset = s["sunset"]

        daylight = (
            sunset - sunrise
        ).total_seconds() / 3600.0

        return SunInfo(
            sunrise=sunrise,
            sunset=sunset,
            daylight_hours=daylight,
        )