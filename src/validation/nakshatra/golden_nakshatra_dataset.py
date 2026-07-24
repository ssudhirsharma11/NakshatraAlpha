"""
Generate Golden Nakshatra Dataset
"""

from datetime import datetime, timedelta
import csv

from src.models.planet import Planet
from src.services.chart_builder import ChartBuilder
from src.astrology.nakshatra import NakshatraEngine

START = datetime(2025, 1, 1, 0, 0)
END = datetime(2025, 12, 31, 18, 0)

STEP = timedelta(hours=6)

LATITUDE = 28.6139
LONGITUDE = 77.2090


def main():

    with open(
        "src/validation/nakshatra/nakshatra_golden.csv",
        "w",
        newline="",
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "timestamp",
            "planet",
            "nakshatra",
            "number",
            "pada",
        ])

        ts = START

        while ts <= END:

            chart = ChartBuilder.build(
                ts,
                LATITUDE,
                LONGITUDE,
            )

            for planet in Planet:

                result = NakshatraEngine.calculate(
                    chart,
                    planet,
                )

                writer.writerow([
                    ts.isoformat(),
                    planet.name,
                    result.nakshatra.name,
                    result.number,
                    result.pada,
                ])

            ts += STEP

    print("Golden Nakshatra dataset generated.")


if __name__ == "__main__":
    main()