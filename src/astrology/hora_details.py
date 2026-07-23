from dataclasses import dataclass
from datetime import datetime

from src.models.planet import Planet


@dataclass(frozen=True)
class HoraDetails:
    """
    Represents one calculated Hora.

    This object contains everything required
    to validate and research Hora calculations.
    """

    # Trading timestamp
    timestamp: datetime

    # Sunrise / Sunset
    sunrise: datetime
    sunset: datetime

    # Hora interval
    hora_number: int

    hora_start: datetime
    hora_end: datetime

    # Planet ruling the Hora
    hora_lord: Planet

    # Day / Night
    is_day_hora: bool

    # Weekday ruler
    day_lord: Planet