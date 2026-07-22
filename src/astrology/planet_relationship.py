"""
Planet Relationship Engine

Calculates relative house positions between planets.

Example

Sun     : Cancer
Saturn  : Pisces

Distance = 9

The result is always between 1 and 12.

1 = Same house/sign
2 = Second
...
12 = Twelfth
"""

from src.models.planet_position import PlanetPosition


def relative_house_distance(
    from_planet: PlanetPosition,
    to_planet: PlanetPosition,
) -> int:
    """
    Returns the relative house/sign distance
    from one planet to another.

    Example

    From : Cancer (4)

    To   : Pisces (12)

    Result = 9
    """

    distance = (
        to_planet.rashi_number
        - from_planet.rashi_number
    ) % 12

    return distance + 1


def is_kendra(distance: int) -> bool:
    """
    Returns True if the distance is a
    Kendra position (1, 4, 7 or 10).
    """

    return distance in (1, 4, 7, 10)


# ------------------------------------------------------------------
# Backward compatibility
# Remove these aliases after all modules have been migrated.
# ------------------------------------------------------------------

relative_sign_distance = relative_house_distance
is_1_4_7_10 = is_kendra