"""
Planet Dignity Engine

Determines the dignity (strength) of a planet
based on the zodiac sign occupied by the planet.
"""

from knowledge.planet_rules import (
    OWN_SIGNS,
    EXALTATION,
    DEBILITATION,
    FRIENDS,
    ENEMIES,
)

from knowledge.sign_info import SIGN_INFO


class PlanetDignity:

    @staticmethod
    def get(planet, sign):
        """
        Returns one of:

        Exalted
        Debilitated
        Own Sign
        Friendly Sign
        Enemy Sign
        Neutral Sign
        """

        # ---------------------------------------
        # Exalted
        # ---------------------------------------

        if sign == EXALTATION[planet]:
            return "Exalted"

        # ---------------------------------------
        # Debilitated
        # ---------------------------------------

        if sign == DEBILITATION[planet]:
            return "Debilitated"

        # ---------------------------------------
        # Own Sign
        # ---------------------------------------

        if sign in OWN_SIGNS[planet]:
            return "Own Sign"

        # ---------------------------------------
        # Sign Lord
        # ---------------------------------------

        sign_lord = SIGN_INFO[sign]["lord"]

        # ---------------------------------------
        # Friendly Sign
        # ---------------------------------------

        if sign_lord in FRIENDS[planet]:
            return "Friendly Sign"

        # ---------------------------------------
        # Enemy Sign
        # ---------------------------------------

        if sign_lord in ENEMIES[planet]:
            return "Enemy Sign"

        # ---------------------------------------
        # Neutral Sign
        # ---------------------------------------

        return "Neutral Sign"