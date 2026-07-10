"""
Application Bootstrap

Responsible for starting NakshatraAlpha.
"""

from core.config import Configuration
from core.logger import get_logger


class Application:

    def __init__(self):
        self.logger = get_logger()

    def start(self):

        self.logger.info("=" * 55)
        self.logger.info("Starting NakshatraAlpha")
        self.logger.info("=" * 55)

        config = Configuration()

        self.logger.info(
            f"Application Version : {config.version}"
        )

        self.logger.info(
            "Bootstrap completed successfully."
        )