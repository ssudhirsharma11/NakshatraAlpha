from datetime import datetime
from zoneinfo import ZoneInfo

from src.features.feature_builder import FeatureBuilder
from src.services.chart_builder import ChartBuilder


def test_feature_builder():

    chart = ChartBuilder().build(
        timestamp=datetime(
            2026,
            7,
            22,
            9,
            15,
            tzinfo=ZoneInfo("Asia/Kolkata"),
        ),
        latitude=28.6139,
        longitude=77.2090,
    )

    features = FeatureBuilder().build(chart)

    print("\n========== DEBUG ==========")
    print("Type:", type(features))
    print("Class:", features.__class__)
    print("Module:", features.__class__.__module__)
    print("Dir:", dir(features))

    if hasattr(features, "__dict__"):
        print("Dict:", features.__dict__)

    print("===========================\n")

    assert features.chart == chart

    assert 1 <= features.saturn_from_sun <= 12

    assert isinstance(
        features.saturn_kendra_from_sun,
        bool,
    )

    print("========== FEATURE SET ==========")
    print(f"Sun      : {chart.sun.rashi}")
    print(f"Saturn   : {chart.saturn.rashi}")
    print(f"Distance : {features.saturn_from_sun}")
    print(f"Kendra   : {features.saturn_kendra_from_sun}")
    print("===============================")