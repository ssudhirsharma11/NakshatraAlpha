"""
Planet Relationship Engine

Calculates relative sign positions between planets.

Example

Sun     : Cancer
Saturn : Pisces

Result = 9

The result is always between 1 and 12.

1 = Same sign
2 = Second sign
...
12 = Twelfth sign
"""


from src.models.planet_position import PlanetPosition


def relative_sign_distance(
    from_planet: PlanetPosition,
    to_planet: PlanetPosition,
) -> int:
    """
    Returns the relative sign distance.

    Example

    From : Cancer (4)

    To   : Pisces (12)

    Distance = 9
    """

    distance = (
        to_planet.rashi_number
        - from_planet.rashi_number
    ) % 12

    return distance + 1


def is_1_4_7_10(distance: int) -> bool:
    """
    Research helper.

    Returns True when distance is
    1,4,7 or 10.
    """

    return distance in (1, 4, 7, 10)