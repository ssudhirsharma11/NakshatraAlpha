from datetime import date

import pytest

from src.config.research_config import RESEARCH_LOCATION
from src.services.sunrise_service import SunriseService


def test_service_exists():
    with pytest.raises(NotImplementedError):
        SunriseService.calculate(
            calculation_date=date(2026, 7, 6),
            location=RESEARCH_LOCATION,
        )