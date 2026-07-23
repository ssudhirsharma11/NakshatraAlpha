from datetime import date

from src.config.research_config import RESEARCH_LOCATION
from src.models.planet import Planet
from src.services.hora_service import HoraService


def test_day_horas_29_june_2026():

    service = HoraService()

    horas = service.get_day_horas(
        calculation_date=date(2026, 6, 29),
        location=RESEARCH_LOCATION,
    )

    assert len(horas) == 12

    assert horas[0].planet == Planet.MOON
    assert horas[1].planet == Planet.SATURN
    assert horas[2].planet == Planet.JUPITER
    assert horas[3].planet == Planet.MARS
    assert horas[4].planet == Planet.SUN