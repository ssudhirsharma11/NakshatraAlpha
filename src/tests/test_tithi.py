"""
Tithi Engine Test
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from src.astrology.tithi import TithiEngine
from src.services.chart_builder import ChartBuilder
from src.models.planet import Planet


def main():

    chart = ChartBuilder.build(
        timestamp=datetime(
            2026,
            7,
            14,
            9,
            45,
            tzinfo=ZoneInfo("Asia/Kolkata"),
        ),
        latitude=28.6139,
        longitude=77.2090,
    )

    result = TithiEngine.calculate(chart)

    sun = chart.get(Planet.SUN)
    moon = chart.get(Planet.MOON)

    print("=" * 70)
    print("TITHI ENGINE TEST")
    print("=" * 70)

    print(f"Sun Longitude      : {sun.longitude:.2f}°")
    print(f"Moon Longitude     : {moon.longitude:.2f}°")
    print(f"Angular Distance   : {result.angular_distance:.2f}°")
    print()

    print(f"Tithi             : {result.tithi.name}")
    print(f"Tithi Number      : {result.number}")
    print(f"Paksha            : {result.paksha}")
    print()

    print(f"Degrees In Tithi  : {result.degrees_in_tithi:.2f}°")
    print(f"Degrees Remaining : {result.degrees_remaining:.2f}°")

    print("=" * 70)


if __name__ == "__main__":
    main()