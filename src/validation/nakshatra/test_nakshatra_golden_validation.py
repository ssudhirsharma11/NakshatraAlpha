"""
Golden Validation - Nakshatra
"""

from datetime import datetime

from src.astrology.nakshatra import NakshatraEngine
from src.models.planet import Planet
from src.services.chart_builder import ChartBuilder
from src.validation.csv_reader import CsvReader
from src.validation.framework.validator import Validator


LATITUDE = 28.6139
LONGITUDE = 77.2090


def main():

    validator = Validator("Nakshatra")

    rows = CsvReader.read(
        "src/validation/nakshatra/nakshatra_golden.csv"
    )

    for row in rows:

        chart = ChartBuilder.build(
            datetime.fromisoformat(
                row["timestamp"]
            ),
            LATITUDE,
            LONGITUDE,
        )

        result = NakshatraEngine.calculate(
            chart,
            Planet[row["planet"]],
        )

        validator.compare(
            row["nakshatra"],
            result.nakshatra.name,
        )

    validator.finish()


if __name__ == "__main__":
    main()