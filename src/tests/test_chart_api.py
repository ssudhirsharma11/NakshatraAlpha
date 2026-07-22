"""
Chart API Test
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.planet import Planet
from src.services.chart_builder import ChartBuilder


def main():

    builder = ChartBuilder()

    chart = builder.build(
        timestamp=datetime(
            2026,
            4,
            27,
            9,
            15,
            tzinfo=ZoneInfo("Asia/Kolkata"),
        ),
        latitude=28.6139,
        longitude=77.2090,
    )

    print("=" * 70)
    print("CHART API TEST")
    print("=" * 70)

    print()

    moon = chart.get(Planet.MOON)

    print("Moon Longitude")
    print(moon.longitude)

    print()

    print("All Planets")

    for planet, position in chart.all_positions().items():
        print(
            f"{planet.name:<10}"
            f"{position.longitude:10.6f}"
        )

    print("=" * 70)


if __name__ == "__main__":
    main()