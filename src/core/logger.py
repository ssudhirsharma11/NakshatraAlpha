import logging


def get_logger():

    logger = logging.getLogger("NakshatraAlpha")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s"
    )

    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger