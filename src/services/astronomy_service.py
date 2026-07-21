"""
Astronomy Service

Responsible for retrieving planetary positions for any given timestamp.
"""

from datetime import datetime

from src.models.planet import Planet
from src.models.planet_position import PlanetPosition
from src.services.ephemeris_service import EphemerisService

class AstronomyService:

    def __init__(self):
        self.initialized = False
        self.ephemeris_loaded = False
        self.ephemeris = EphemerisService()

    def initialize(self):
        """Initialize astronomy engine."""
        self.initialized = True

    def load_ephemeris(self):
        """Load astronomical ephemeris."""
        self.ephemeris_loaded = True

    def status(self) -> str:

        if self.initialized:
            return "√ Astronomy Service Ready"

        return "X Astronomy Service Not Initialized"

    def get_planet_positions(
        self,
        timestamp: datetime,
    ) -> list[PlanetPosition]:
        """
        Returns planetary positions for the supplied timestamp.

        Parameters
        ----------
        timestamp : datetime
            Time for which planetary positions are required.
            Should preferably be timezone-aware.

        Returns
        -------
        list[PlanetPosition]
        """

        if not self.initialized:
            raise RuntimeError(
                "Astronomy Service not initialized."
            )

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

        positions = []

        for planet in planets:

            longitude = self.ephemeris.get_longitude(
                planet,
                timestamp,
            )

            positions.append(
                PlanetPosition(
                    planet=planet,
                    longitude=longitude,
                    latitude=0.0,
                    distance=0.0,
                    speed=0.0,
                )
            )

        return positions