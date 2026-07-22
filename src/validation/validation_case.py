"""
Validation Case Model
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ValidationCase:
    """
    Represents one external validation case.
    """

    timestamp: datetime

    latitude: float

    longitude: float

    expected_tithi: str | None = None

    expected_nakshatra: str | None = None