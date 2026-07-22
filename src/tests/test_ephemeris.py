"""
Test Ephemeris Service
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from src.models.planet import Planet
from src.services.ephemeris_service import EphemerisService


def main():

    print("=" * 65)
    print("           EPHEMERIS SERVICE TEST")
    print("=" * 65)

    timestamp = datetime(
        2026,
        4,
        27,
        9,
        15,
        tzinfo=ZoneInfo("Asia/Kolkata"),
    )

    ephemeris = EphemerisService()

    planets = [
        Planet.SUN,
        Planet.MOON,
        Planet.MERCURY,
        Planet.VENUS,
        Planet.MARS,
        Planet.JUPITER,
        Planet.SATURN,
        Planet.RAHU,
        Planet.KETU,
    ]

    for planet in planets:

        position = ephemeris.get_position(
            planet,
            timestamp,
        )

        print(
            f"{planet.name:<10}"
            f"Lon: {position.longitude:10.6f}°   "
            f"Lat: {position.latitude:9.6f}°   "
            f"Dist: {position.distance:10.6f}   "
            f"Speed: {position.speed:10.6f}"
        )

    print("=" * 65)



if __name__ == "__main__":
    main()