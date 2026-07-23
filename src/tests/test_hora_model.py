from datetime import datetime

from src.models.hora import Hora
from src.models.planet import Planet


def test_hora_model():

    hora = Hora(
        index=1,
        planet=Planet.MOON,
        start=datetime(2026, 6, 29, 5, 3),
        end=datetime(2026, 6, 29, 6, 11),
        is_day=True,
    )

    assert hora.index == 1
    assert hora.planet == Planet.MOON
    assert hora.is_day is True
    assert hora.duration_seconds > 0