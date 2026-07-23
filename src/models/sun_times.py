from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class SunTimes:
    """
    Astronomical information for a single calendar date.
    """

    sunrise: datetime
    sunset: datetime

    solar_noon: datetime

    day_length: timedelta
    night_length: timedelta