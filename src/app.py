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
from astrology.hora import HoraCalculator
from astrology.planet_dignity import PlanetDignity


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

        # -------------------------------------------------
        # Current Panchang
        # -------------------------------------------------

        tithi = TithiCalculator().get()
        hora = HoraCalculator().get()

        self.logger.info("")
        self.logger.info("Current Panchang")
        self.logger.info("----------------------------------")

        self.logger.info(f"Paksha      : {tithi.paksha}")
        self.logger.info(f"Tithi       : {tithi.name}")
        self.logger.info(f"Tithi Group : {tithi.group}")
        self.logger.info(f"Tithi Lord  : {tithi.lord}")

        self.logger.info("")
        self.logger.info("Current Hora")
        self.logger.info("----------------------------------")

        self.logger.info(f"Weekday     : {hora.weekday}")
        self.logger.info(f"Hora Number : {hora.number}")
        self.logger.info(f"Hora Lord   : {hora.lord}")
        self.logger.info(f"Next Hora   : {hora.next_lord}")

        self.logger.info("")

        # -------------------------------------------------
        # Planetary Positions & Dignity
        # -------------------------------------------------

        self.logger.info("Planetary Positions & Dignity")
        self.logger.info("--------------------------------------------------------------------------")

        for planet in positions:

            sign = Zodiac.sign(planet.longitude)
            nakshatra = Nakshatra.get(planet.longitude)

            dignity = PlanetDignity.get(
                planet.planet,
                sign,
            )

            self.logger.info(
                f"{planet.planet.value:9}"
                f"{planet.longitude:8.2f}°   "
                f"{sign:12}"
                f"{nakshatra:20}"
                f"{dignity}"
            )

        self.logger.info("")

        self.logger.info(
            f"Application Version : {config.version}"
        )

        self.logger.info(
            "Bootstrap completed successfully."
        )