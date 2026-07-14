"""
Application Bootstrap

Responsible for starting NakshatraAlpha.
"""

from core.config import Configuration
from core.logger import get_logger

from services.astronomy_service import AstronomyService

from astrology.zodiac import Zodiac
from astrology.nakshatra import Nakshatra
from astrology.tithi import TithiCalculator


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

        # -----------------------------
        # Current Panchang
        # -----------------------------
        tithi = TithiCalculator().get()

        self.logger.info("")
        self.logger.info("Current Panchang")
        self.logger.info("----------------------------------")
        self.logger.info(f"Paksha      : {tithi.paksha}")
        self.logger.info(f"Tithi       : {tithi.name}")
        self.logger.info(f"Tithi Group : {tithi.group}")
        self.logger.info(f"Tithi Lord  : {tithi.lord}")
        self.logger.info("")

        # -----------------------------
        # Planetary Positions
        # -----------------------------
        self.logger.info("Planetary Positions")
        self.logger.info("----------------------------------")

        for planet in positions:

            sign = Zodiac.sign(planet.longitude)
            nakshatra = Nakshatra.get(planet.longitude)

            self.logger.info(
                f"{planet.planet.value:8} "
                f"{planet.longitude:7.2f}°   "
                f"{sign:8} "
                f"{nakshatra}"
            )

        self.logger.info("")

        self.logger.info(
            f"Application Version : {config.version}"
        )

        self.logger.info(
            "Bootstrap completed successfully."
        )