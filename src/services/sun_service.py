"""
Sun Service

Responsible for sunrise, sunset and daylight calculations.
"""

from dataclasses import dataclass
from datetime import date, datetime

from astral import LocationInfo
from astral.sun import sun
from zoneinfo import ZoneInfo

from src.config.research_config import RESEARCH_LOCATION
from src.models.location import Location


@dataclass(frozen=True)
class SunInfo:
    sunrise: datetime
    sunset: datetime
    daylight_hours: float


class SunService:

    def get(
        self,
        calculation_date: date | None = None,
        location: Location | None = None,
    ) -> SunInfo:
        """
        Returns sunrise/sunset information for the requested date and location.

        If no date/location is supplied, the research defaults are used.
        """

        if location is None:
            location = RESEARCH_LOCATION

        tz = ZoneInfo(location.timezone)

        if calculation_date is None:
            calculation_date = datetime.now(tz).date()

        astral_location = LocationInfo(
            name=location.name,
            region="India",
            timezone=location.timezone,
            latitude=location.latitude,
            longitude=location.longitude,
        )

        s = sun(
            observer=astral_location.observer,
            date=calculation_date,
            tzinfo=tz,
        )

        sunrise = s["sunrise"]
        sunset = s["sunset"]

        daylight = (sunset - sunrise).total_seconds() / 3600.0

        return SunInfo(
            sunrise=sunrise,
            sunset=sunset,
            daylight_hours=daylight,
        )