"""
Feature Builder Integration Tests
"""

from datetime import datetime, timezone

from src import features
from src.features.feature_builder import FeatureBuilder
from src.services.chart_builder import ChartBuilder


def test_feature_builder_populates_core_features():
    """
    Ensure FeatureBuilder populates the
    major research fields correctly.
    """

    chart = ChartBuilder.build(
        timestamp=datetime(
            2026,
            1,
            1,
            9,
            15,
            tzinfo=timezone.utc,
        ),
        latitude=28.6139,
        longitude=77.2090,
    )

    features = FeatureBuilder().build(chart)

    # Calendar
    assert features.weekday is not None
    # Tithi
    assert features.tithi is not None
    assert 1 <= features.tithi_number <= 30
    assert features.paksha is not None

    # Lagna
    assert features.lagna_sign is not None
    assert features.lagna_number is not None
    assert features.lagna_degree is not None

    # Nakshatra
    assert features.moon_nakshatra is not None
    assert 1 <= features.moon_nakshatra_number <= 27

    assert features.sun_nakshatra is not None
    assert 1 <= features.sun_nakshatra_number <= 27

    assert 1 <= features.pada <= 4

    # Planet Positions
    assert features.sun_sign is not None
    assert features.moon_sign is not None

    # Relationships
    assert features.saturn_from_sun is not None
    assert isinstance(
        features.saturn_kendra_from_sun,
        bool,
    )