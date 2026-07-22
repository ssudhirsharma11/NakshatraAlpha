from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.planet import Planet
from src.services.ephemeris_service import EphemerisService

service = EphemerisService()

timestamp = datetime(
    2026,
    7,
    22,
    9,
    15,
    tzinfo=ZoneInfo("Asia/Kolkata"),
)

for planet in Planet:
    pos = service.get_position(planet, timestamp)

    print("=" * 60)
    print(pos)