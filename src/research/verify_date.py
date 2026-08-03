def verify_day(
    self,
    report_date: date,
):

    horas = self.hora_service.get_day_horas(
        report_date,
        RESEARCH_LOCATION,
    )

    for hora in horas:

        if (
            REPORT_HORA is not None
            and hora.index != REPORT_HORA
        ):
            continue

        try:

            self._verify_hora(hora)

        except ValueError as ex:

            if "No market candles found" in str(ex):
                continue

            raise