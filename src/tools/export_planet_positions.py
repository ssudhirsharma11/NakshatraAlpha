from datetime import datetime
from zoneinfo import ZoneInfo

from src.config.research_config import RESEARCH_LOCATION
from src.services.planet_position_service import PlanetPositionService

service = PlanetPositionService()

positions = service.get_positions(
    datetime(
        2026,
        6,
        29,
        9,
        0,
        tzinfo=ZoneInfo("Asia/Kolkata"),
    ),
    RESEARCH_LOCATION,
)

for planet, position in positions.items():
    print(
        f"{planet.name:8} "
        f"{position.longitude:.8f} "
        f"{position.latitude:.8f} "
        f"{position.speed:.8f}"
    )