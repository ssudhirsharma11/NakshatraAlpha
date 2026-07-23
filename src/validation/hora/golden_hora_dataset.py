from dataclasses import dataclass
from datetime import date, time

from src.models.planet import Planet


@dataclass(frozen=True)
class ExpectedHora:
    index: int
    planet: Planet
    start: time
    end: time


GOLDEN_HORA_DATASET = {
    date(2026, 6, 29): [
        ExpectedHora(1, Planet.MOON,     time(5, 3),  time(6, 11)),
        ExpectedHora(2, Planet.SATURN,   time(6, 11), time(7, 18)),
        ExpectedHora(3, Planet.JUPITER,  time(7, 18), time(8, 26)),
        ExpectedHora(4, Planet.MARS,     time(8, 26), time(9, 34)),
        ExpectedHora(5, Planet.SUN,      time(9, 34), time(10, 41)),
        ExpectedHora(6, Planet.VENUS,    time(10, 41), time(11, 49)),
        ExpectedHora(7, Planet.MERCURY,  time(11, 49), time(12, 56)),
        ExpectedHora(8, Planet.MOON,     time(12, 56), time(14, 4)),
        ExpectedHora(9, Planet.SATURN,   time(14, 4), time(15, 12)),
        ExpectedHora(10, Planet.JUPITER, time(15, 12), time(16, 19)),
        ExpectedHora(11, Planet.MARS,    time(16, 19), time(17, 27)),
        ExpectedHora(12, Planet.SUN,     time(17, 27), time(18, 34)),
    ]
}