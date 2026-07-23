from src.models.location import Location

# Default research location
# All astrology calculations will use this location unless
# explicitly overridden.

RESEARCH_LOCATION = Location(
    name="Jamshedpur",
    latitude=22.8046,
    longitude=86.2029,
    timezone="Asia/Kolkata",
)