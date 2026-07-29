from datetime import date, datetime

from src.models.hora import Hora
from src.models.location import Location
from src.models.planet import Planet
from src.services.sun_service import SunService


class HoraService:
    """
    Computes daytime Hora periods and returns
    the active Hora for a given timestamp.
    """

    HORA_SEQUENCE = (
        Planet.MARS,
        Planet.SUN,
        Planet.VENUS,
        Planet.MERCURY,
        Planet.MOON,
        Planet.SATURN,
        Planet.JUPITER,
    )

    WEEKDAY_LORD = {
        0: Planet.MOON,      # Monday
        1: Planet.MARS,      # Tuesday
        2: Planet.MERCURY,   # Wednesday
        3: Planet.JUPITER,   # Thursday
        4: Planet.VENUS,     # Friday
        5: Planet.SATURN,    # Saturday
        6: Planet.SUN,       # Sunday
    }

    def __init__(
        self,
        sun_service: SunService | None = None,
    ):
        self.sun_service = sun_service or SunService()

    def get_day_horas(
        self,
        calculation_date: date,
        location: Location,
    ) -> list[Hora]:
        """
        Returns the 12 daytime Hora periods
        for the supplied date.
        """

        sun = self.sun_service.get(
            calculation_date=calculation_date,
            location=location,
        )

        sunrise = sun.sunrise
        sunset = sun.sunset

        hora_length = (sunset - sunrise) / 12

        weekday_lord = self.WEEKDAY_LORD[
            calculation_date.weekday()
        ]

        start_index = self.HORA_SEQUENCE.index(
            weekday_lord
        )

        horas: list[Hora] = []

        current_start = sunrise

        for i in range(12):

            current_end = current_start + hora_length

            planet = self.HORA_SEQUENCE[
                (start_index + i)
                % len(self.HORA_SEQUENCE)
            ]

            horas.append(
                Hora(
                    index=i + 1,
                    planet=planet,
                    start=current_start,
                    end=current_end,
                    is_day=True,
                )
            )

            current_start = current_end

        return horas

    def get_hora(
        self,
        timestamp: datetime,
        location: Location,
    ) -> Hora:
        """
        Returns the active daytime Hora
        for the supplied timestamp.

        Raises
        ------
        ValueError
            If timestamp is outside the
            daytime Hora interval.
        """

        horas = self.get_day_horas(
            calculation_date=timestamp.date(),
            location=location,
        )

        for hora in horas:

            if hora.start <= timestamp < hora.end:
                return hora

        # Handle the exact sunset boundary by returning the final Hora.
        if horas and timestamp == horas[-1].end:
            return horas[-1]

        raise ValueError(
            f"No daytime Hora found for timestamp {timestamp}."
        )