"""
Astronomy Service

Responsible for astronomical calculations.
"""

from services.ephemeris_service import EphemerisService
from models.planet import Planet
from models.planet_position import PlanetPosition


class AstronomyService:

    def __init__(self):
        self.initialized = False
        self.ephemeris_loaded = False

    def initialize(self):
        """Initialize astronomy engine."""
        self.initialized = True

    def load_ephemeris(self):
        """Load astronomical ephemeris."""
        self.ephemeris_loaded = True

    def status(self):

        if self.initialized:
            return "√ Astronomy Service Ready"

        return "X Astronomy Service Not Initialized"

    def get_planet_positions(self):

        if not self.initialized:
            raise RuntimeError("Astronomy Service not initialized.")

        ephemeris = EphemerisService()
        sun_longitude = ephemeris.current_sun_longitude()

        return [
            PlanetPosition(Planet.SUN, sun_longitude, 0.0, 0.98),
            PlanetPosition(Planet.MOON, 220.1, 5.2, 13.2),
            PlanetPosition(Planet.MERCURY, 150.4, 1.0, 1.1),
            PlanetPosition(Planet.VENUS, 45.3, 0.5, 1.2),
            PlanetPosition(Planet.MARS, 300.7, -1.2, 0.5),
            PlanetPosition(Planet.JUPITER, 20.8, -0.1, 0.08),
            PlanetPosition(Planet.SATURN, 330.2, 0.3, 0.03),
            PlanetPosition(Planet.RAHU, 180.0, 0.0, -0.05),
            PlanetPosition(Planet.KETU, 0.0, 0.0, -0.05),
        ]