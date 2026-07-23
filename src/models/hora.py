from dataclasses import dataclass
from datetime import datetime

from src.models.planet import Planet


@dataclass(frozen=True)
class Hora:
    """
    Represents a single Hora period.

    Attributes
    ----------
    index:
        Hora number within the day/night (1-12)

    planet:
        Planet ruling this Hora.

    start:
        Hora start time.

    end:
        Hora end time.

    is_day:
        True if this is one of the 12 daytime Horas,
        False for the 12 nighttime Horas.
    """

    index: int
    planet: Planet
    start: datetime
    end: datetime
    is_day: bool

    @property
    def duration_seconds(self) -> float:
        return (self.end - self.start).total_seconds()