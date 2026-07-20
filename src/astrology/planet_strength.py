"""
Planet Strength Engine

Sprint 19B

Calculates a numerical strength score for a planet
based on its current dignity.

Future versions will include:

- House Strength
- Combustion
- Retrograde
- Aspects
- Dig Bala
- Shadbala
- Nakshatra Strength
"""

from dataclasses import dataclass

from astrology.planet_dignity import PlanetDignity


@dataclass(frozen=True)
class StrengthResult:
    """
    Result returned by PlanetStrength.get()
    """

    score: int
    dignity: str
    rating: str


class PlanetStrength:
    """
    Calculates planet strength.

    Version 1 (Sprint 19B)

    Uses only Sign Dignity.
    """

    # Numerical score mapping
    SCORES = {
        "Exalted": 100,
        "Own Sign": 90,
        "Friendly Sign": 75,
        "Neutral Sign": 60,
        "Enemy Sign": 40,
        "Debilitated": 20,
    }

    @classmethod
    def get(cls, planet, sign) -> StrengthResult:

        dignity = PlanetDignity.get(
            planet,
            sign,
        )

        score = cls.SCORES.get(
            dignity,
            0,
        )

        rating = cls._rating(score)

        return StrengthResult(
            score=score,
            dignity=dignity,
            rating=rating,
        )

    @staticmethod
    def _rating(score: int) -> str:
        """
        Converts numerical score
        into a human readable rating.
        """

        if score >= 90:
            return "Excellent"

        if score >= 75:
            return "Strong"

        if score >= 60:
            return "Average"

        if score >= 40:
            return "Weak"

        return "Very Weak"