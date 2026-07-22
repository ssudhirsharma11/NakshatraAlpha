"""
Nakshatra Engine Test
"""

from datetime import datetime

from zoneinfo import ZoneInfo

from src.astrology.nakshatra import NakshatraEngine
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

    print("=" * 70)
    print("NAKSHATRA ENGINE TEST")
    print("=" * 70)

    for planet in Planet:

        result = NakshatraEngine.calculate(
            chart,
            planet,
        )

        print(
    f"{planet.name:<10}"
    f"{result.nakshatra.name:<20}"
    f"Pada {result.pada}   "
    f"Lord {result.lord.name:<8} "
    f"In {result.degrees_in_nakshatra:6.2f}°   "
    f"Remain {result.degrees_remaining:6.2f}°"
    )

    print("=" * 70)


if __name__ == "__main__":
    main()