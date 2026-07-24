"""
Generate a golden Tithi dataset.

This file creates a CSV containing the expected Tithi values for a range
of timestamps. The dataset becomes the regression baseline.
"""

from datetime import datetime, timedelta
import csv

from src.models.planet import Planet
from src.services.chart_builder import ChartBuilder
from src.astrology.tithi import TithiEngine


START = datetime(2025, 1, 1, 0, 0)
END = datetime(2025, 12, 31, 23, 0)
STEP = timedelta(hours=6)

LATITUDE = 28.6139
LONGITUDE = 77.2090


def generate():

    with open(
        "src/validation/tithi/tithi_golden.csv",
        "w",
        newline="",
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "timestamp",
            "sun_longitude",
            "moon_longitude",
            "angular_distance",
            "tithi_number",
            "tithi_name",
            "paksha",
        ])

        ts = START

        while ts <= END:

            chart = ChartBuilder.build(
                ts,
                LATITUDE,
                LONGITUDE,
            )

            result = TithiEngine.calculate(chart)

            sun = chart.sun.longitude
            moon = chart.moon.longitude

            angle = (moon - sun) % 360

            writer.writerow([
                ts.isoformat(),
                round(sun, 6),
                round(moon, 6),
                round(angle, 6),
                result.number,
                result.tithi.name,
                result.paksha,
            ])

            ts += STEP

    print("Golden dataset generated.")


if __name__ == "__main__":
    generate()