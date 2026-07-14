"""
Location Model

Represents a geographical location used for
astronomical calculations.
"""

from dataclasses import dataclass


@dataclass
class Location:

    city: str
    latitude: float
    longitude: float
    timezone: str