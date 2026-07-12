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

        return [
            PlanetPosition(
                Planet.SUN,
                ephemeris.current_longitude(Planet.SUN),
                0.0,
                0.98,
            ),
            PlanetPosition(
                Planet.MOON,
                ephemeris.current_longitude(Planet.MOON),
                5.2,
                13.2,
            ),
            PlanetPosition(
                Planet.MERCURY,
                ephemeris.current_longitude(Planet.MERCURY),
                1.0,
                1.1,
            ),
            PlanetPosition(
                Planet.VENUS,
                ephemeris.current_longitude(Planet.VENUS),
                0.5,
                1.2,
            ),
            PlanetPosition(
                Planet.MARS,
                ephemeris.current_longitude(Planet.MARS),
                -1.2,
                0.5,
            ),
            PlanetPosition(
                Planet.JUPITER,
                ephemeris.current_longitude(Planet.JUPITER),
                -0.1,
                0.08,
            ),
            PlanetPosition(
                Planet.SATURN,
                ephemeris.current_longitude(Planet.SATURN),
                0.3,
                0.03,
            ),
            PlanetPosition(
                Planet.RAHU,
                ephemeris.current_longitude(Planet.RAHU),
                0.0,
                -0.05,
            ),
            PlanetPosition(
                Planet.KETU,
                ephemeris.current_longitude(Planet.KETU),
                0.0,
                -0.05,
            ),
        ]