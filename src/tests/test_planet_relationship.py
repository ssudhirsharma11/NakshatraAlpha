from src.astrology.planet_relationship import (
    is_1_4_7_10,
    relative_sign_distance,
)
from src.models.planet import Planet
from src.models.planet_position import PlanetPosition


def make_position(sign_number: int):

    return PlanetPosition(
        planet=Planet.SUN,
        longitude=0,
        latitude=0,
        distance=0,
        speed=0,

        rashi="Dummy",
        rashi_number=sign_number,
        degrees_in_rashi=0,

        navamsha="Dummy",
        navamsha_number=1,
        navamsha_lord=Planet.SUN,
    )


def test_same_sign():

    assert relative_sign_distance(
        make_position(4),
        make_position(4),
    ) == 1


def test_fourth():

    assert relative_sign_distance(
        make_position(4),
        make_position(7),
    ) == 4


def test_seventh():

    assert relative_sign_distance(
        make_position(4),
        make_position(10),
    ) == 7


def test_tenth():

    assert relative_sign_distance(
        make_position(4),
        make_position(1),
    ) == 10


def test_wraparound():

    assert relative_sign_distance(
        make_position(12),
        make_position(1),
    ) == 2


def test_research_filter():

    assert is_1_4_7_10(1)
    assert is_1_4_7_10(4)
    assert is_1_4_7_10(7)
    assert is_1_4_7_10(10)

    assert not is_1_4_7_10(2)
    assert not is_1_4_7_10(3)
    assert not is_1_4_7_10(5)
    assert not is_1_4_7_10(6)
    assert not is_1_4_7_10(8)
    assert not is_1_4_7_10(9)
    assert not is_1_4_7_10(11)
    assert not is_1_4_7_10(12)