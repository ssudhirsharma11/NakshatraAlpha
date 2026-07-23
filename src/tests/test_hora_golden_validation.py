from datetime import date

from src.config.research_config import RESEARCH_LOCATION
from src.services.hora_service import HoraService
from src.validation.hora.golden_hora_dataset import GOLDEN_HORA_DATASET


def minutes_since_midnight(t):
    return t.hour * 60 + t.minute


def test_golden_hora_dataset():

    service = HoraService()

    for calculation_date, expected_horas in GOLDEN_HORA_DATASET.items():

        calculated = service.get_day_horas(
            calculation_date=calculation_date,
            location=RESEARCH_LOCATION,
        )

        assert len(calculated) == len(expected_horas)

        for actual, expected in zip(calculated, expected_horas):

            assert actual.index == expected.index
            assert actual.planet == expected.planet

            actual_start = minutes_since_midnight(actual.start.time())
            expected_start = minutes_since_midnight(expected.start)

            actual_end = minutes_since_midnight(actual.end.time())
            expected_end = minutes_since_midnight(expected.end)

            # Allow ±1 minute due to rounding
            assert abs(actual_start - expected_start) <= 1
            assert abs(actual_end - expected_end) <= 1