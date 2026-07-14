"""
Hora Calculator
"""

from dataclasses import dataclass
from datetime import datetime

from knowledge.hora_sequence import (
    FIRST_HORA,
    HORA_SEQUENCE,
)


@dataclass
class Hora:

    number: int
    lord: str
    next_lord: str
    weekday: str


class HoraCalculator:

    def get(self):

        now = datetime.now()

        weekday = now.strftime("%A")

        first_lord = FIRST_HORA[weekday]

        index = HORA_SEQUENCE.index(first_lord)

        # Temporary approximation:
        # Each Hora = 60 minutes.
        # In Sprint 17 we'll replace this with
        # sunrise/sunset based unequal Hora.

        hora_number = now.hour % 24

        current_index = (
            index + hora_number
        ) % len(HORA_SEQUENCE)

        next_index = (
            current_index + 1
        ) % len(HORA_SEQUENCE)

        return Hora(
            number=hora_number + 1,
            lord=HORA_SEQUENCE[current_index],
            next_lord=HORA_SEQUENCE[next_index],
            weekday=weekday,
        )