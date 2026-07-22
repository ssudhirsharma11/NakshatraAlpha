from datetime import datetime
from zoneinfo import ZoneInfo

from src.features.feature_builder import FeatureBuilder
from src.services.chart_builder import ChartBuilder


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

    features = FeatureBuilder.build(chart)

    print()

    print("=" * 60)
    print("FEATURE SET")
    print("=" * 60)

    print(features)


if __name__ == "__main__":
    main()