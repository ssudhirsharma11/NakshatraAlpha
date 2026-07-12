"""
Application Bootstrap

Responsible for starting NakshatraAlpha.
"""

from core.config import Configuration
from core.logger import get_logger
from services.astronomy_service import AstronomyService


class Application:

    def __init__(self):
        self.logger = get_logger()

    def start(self):

        self.logger.info("=" * 55)
        self.logger.info("Starting NakshatraAlpha")
        self.logger.info("=" * 55)

        config = Configuration()
        astronomy = AstronomyService()

        astronomy.initialize()
        astronomy.load_ephemeris()

        self.logger.info(astronomy.status())

        positions = astronomy.get_planet_positions()

        self.logger.info(f"Loaded {len(positions)} planetary objects.")

        for planet in positions:
            self.logger.info(
                f"{planet.planet.value:8} {planet.longitude:7.2f}°"
            )

        self.logger.info(
            f"Application Version : {config.version}"
        )

        self.logger.info(
            "Bootstrap completed successfully."
        )