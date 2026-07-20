"""
Application Bootstrap

Responsible for starting NakshatraAlpha.
"""

from core.config import Configuration
from core.logger import get_logger

from services.astronomy_service import AstronomyService
from services.sun_service import SunService

from astrology.zodiac import Zodiac
from astrology.nakshatra import Nakshatra
from astrology.tithi import TithiCalculator
from astrology.hora import HoraCalculator
from astrology.planet_dignity import PlanetDignity
from astrology.planet_strength import PlanetStrength


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
        sun = SunService().get()

        self.logger.info("")
        self.logger.info("Current Panchang")
        self.logger.info("----------------------------------")
        self.logger.info(f"Paksha      : {tithi.paksha}")
        self.logger.info(f"Tithi       : {tithi.name}")
        self.logger.info(f"Tithi Group : {tithi.group}")
        self.logger.info(f"Tithi Lord  : {tithi.lord}")

        # -------------------------------------------------
        # Current Hora
        # -------------------------------------------------

        self.logger.info("")
        self.logger.info("Current Hora")
        self.logger.info("----------------------------------")
        self.logger.info(f"Weekday     : {hora.weekday}")
        self.logger.info(f"Hora Number : {hora.number}")
        self.logger.info(f"Hora Lord   : {hora.lord}")
        self.logger.info(f"Next Hora   : {hora.next_lord}")

        # -------------------------------------------------
        # Current Sun
        # -------------------------------------------------

        self.logger.info("")
        self.logger.info("Current Sun")
        self.logger.info("----------------------------------")
        self.logger.info(f"Sunrise     : {sun.sunrise.strftime('%H:%M:%S')}")
        self.logger.info(f"Sunset      : {sun.sunset.strftime('%H:%M:%S')}")
        self.logger.info(f"Daylight    : {sun.daylight_hours:.2f} hrs")

        # -------------------------------------------------
        # Planetary Positions & Dignity
        # -------------------------------------------------

        self.logger.info("")
        self.logger.info("Planetary Positions & Dignity")
        self.logger.info("-" * 82)

        self.logger.info(
            f"{'Planet':<10}"
            f"{'Longitude':>10}   "
            f"{'Sign':<12}"
            f"{'Nakshatra':<22}"
            f"{'Dignity'}"
        )

        self.logger.info("-" * 82)

        for planet in positions:

            sign = Zodiac.sign(planet.longitude)
            nakshatra = Nakshatra.get(planet.longitude)

            dignity = PlanetDignity.get(
                planet.planet,
                sign,
            )

            self.logger.info(
                f"{planet.planet.value:<10}"
                f"{planet.longitude:>9.2f}°   "
                f"{sign:<12}"
                f"{nakshatra:<22}"
                f"{dignity:<20}"
            )

        # -------------------------------------------------
        # Planet Strength
        # -------------------------------------------------

        self.logger.info("")
        self.logger.info("Planet Strength")
        self.logger.info("-" * 55)

        self.logger.info(
            f"{'Planet':<10}"
            f"{'Score':>8}"
            f"{'Rating':>18}"
        )

        self.logger.info("-" * 55)

        for planet in positions:

            sign = Zodiac.sign(planet.longitude)

            strength = PlanetStrength.get(
                planet.planet,
                sign,
            )

            self.logger.info(
                f"{planet.planet.value:<10}"
                f"{strength.score:>8}"
                f"{strength.rating:>18}"
            )

        self.logger.info("")
        self.logger.info(f"Application Version : {config.version}")
        self.logger.info("Bootstrap completed successfully.")