from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    """
    Represents a geographical location used for astronomical
    and astrological calculations.
    """

    name: str
    latitude: float
    longitude: float
    timezone: str