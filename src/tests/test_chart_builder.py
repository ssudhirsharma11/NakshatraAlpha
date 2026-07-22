"""
Test Chart Builder
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from src.services.chart_builder import ChartBuilder


def main():

    print("=" * 70)
    print("               CHART BUILDER TEST")
    print("=" * 70)

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

    print(f"Julian Day : {chart.julian_day:.6f}")
    print()

    print(f"Sun      : {chart.sun.longitude:.6f}°")
    print(f"Moon     : {chart.moon.longitude:.6f}°")
    print(f"Mercury  : {chart.mercury.longitude:.6f}°")
    print(f"Venus    : {chart.venus.longitude:.6f}°")
    print(f"Mars     : {chart.mars.longitude:.6f}°")
    print(f"Jupiter  : {chart.jupiter.longitude:.6f}°")
    print(f"Saturn   : {chart.saturn.longitude:.6f}°")
    print(f"Rahu     : {chart.rahu.longitude:.6f}°")
    print(f"Ketu     : {chart.ketu.longitude:.6f}°")

    print("=" * 70)


if __name__ == "__main__":
    main()