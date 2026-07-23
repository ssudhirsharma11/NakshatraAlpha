from datetime import datetime
from zoneinfo import ZoneInfo

from src.config.research_config import RESEARCH_LOCATION
from src.models.planet import Planet
from src.services.planet_position_service import PlanetPositionService


def test_planet_positions():

    service = PlanetPositionService()

    dt = datetime(
        2026,
        6,
        29,
        9,
        0,
        tzinfo=ZoneInfo("Asia/Kolkata"),
    )

    positions = service.get_positions(
        dt,
        RESEARCH_LOCATION,
    )

    expected_planets = {
        Planet.SUN,
        Planet.MOON,
        Planet.MARS,
        Planet.MERCURY,
        Planet.JUPITER,
        Planet.VENUS,
        Planet.SATURN,
    }

    assert set(positions.keys()) == expected_planets

    for position in positions.values():

        assert 0 <= position.longitude < 360
        assert -90 <= position.latitude <= 90
        assert isinstance(position.speed, float)
        assert isinstance(position.is_retrograde, bool)