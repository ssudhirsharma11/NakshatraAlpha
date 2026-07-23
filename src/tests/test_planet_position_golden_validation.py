from src.config.research_config import RESEARCH_LOCATION
from src.services.planet_position_service import PlanetPositionService

from src.validation.planets.golden_planet_positions import (
    GOLDEN_PLANET_POSITIONS,
    REFERENCE_DATETIME,
)


TOLERANCE = 1e-6


def test_planet_position_golden_dataset():

    service = PlanetPositionService()

    positions = service.get_positions(
        REFERENCE_DATETIME,
        RESEARCH_LOCATION,
    )

    for planet, expected in GOLDEN_PLANET_POSITIONS.items():

        actual = positions[planet]

        assert abs(actual.longitude - expected.longitude) < TOLERANCE
        assert abs(actual.latitude - expected.latitude) < TOLERANCE
        assert abs(actual.speed - expected.speed) < TOLERANCE