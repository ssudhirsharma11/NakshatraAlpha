from src.config.research_config import RESEARCH_LOCATION


def test_default_location():
    assert RESEARCH_LOCATION.name == "Jamshedpur"
    assert RESEARCH_LOCATION.latitude == 22.8046
    assert RESEARCH_LOCATION.longitude == 86.2029
    assert RESEARCH_LOCATION.timezone == "Asia/Kolkata"