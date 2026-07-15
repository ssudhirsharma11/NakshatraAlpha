"""
Planet Rules

Static planetary dignity rules used by the
Planet Dignity Engine.

Contains NO calculations.
"""

from models.planet import Planet


# ---------------------------------------------------------
# Own Signs
# ---------------------------------------------------------

OWN_SIGNS = {

    Planet.SUN: ["Leo"],

    Planet.MOON: ["Cancer"],

    Planet.MARS: [
        "Aries",
        "Scorpio",
    ],

    Planet.MERCURY: [
        "Gemini",
        "Virgo",
    ],

    Planet.JUPITER: [
        "Sagittarius",
        "Pisces",
    ],

    Planet.VENUS: [
        "Taurus",
        "Libra",
    ],

    Planet.SATURN: [
        "Capricorn",
        "Aquarius",
    ],

    # Research Convention
    Planet.RAHU: [
        "Aquarius",
    ],

    Planet.KETU: [
        "Scorpio",
    ],
}


# ---------------------------------------------------------
# Exaltation
# ---------------------------------------------------------

EXALTATION = {

    Planet.SUN: "Aries",

    Planet.MOON: "Taurus",

    Planet.MARS: "Capricorn",

    Planet.MERCURY: "Virgo",

    Planet.JUPITER: "Cancer",

    Planet.VENUS: "Pisces",

    Planet.SATURN: "Libra",

    Planet.RAHU: "Taurus",

    Planet.KETU: "Scorpio",
}


# ---------------------------------------------------------
# Debilitation
# ---------------------------------------------------------

DEBILITATION = {

    Planet.SUN: "Libra",

    Planet.MOON: "Scorpio",

    Planet.MARS: "Cancer",

    Planet.MERCURY: "Pisces",

    Planet.JUPITER: "Capricorn",

    Planet.VENUS: "Virgo",

    Planet.SATURN: "Aries",

    Planet.RAHU: "Scorpio",

    Planet.KETU: "Taurus",
}


# ---------------------------------------------------------
# Friends
# ---------------------------------------------------------

FRIENDS = {

    Planet.SUN: [
        Planet.MOON,
        Planet.MARS,
        Planet.JUPITER,
    ],

    Planet.MOON: [
        Planet.SUN,
        Planet.MARS,
        Planet.JUPITER,
    ],

    Planet.MARS: [
        Planet.SUN,
        Planet.MOON,
        Planet.JUPITER,
    ],

    Planet.MERCURY: [
        Planet.VENUS,
        Planet.SATURN,
    ],

    Planet.JUPITER: [
        Planet.SUN,
        Planet.MOON,
        Planet.MARS,
    ],

    Planet.VENUS: [
        Planet.MERCURY,
        Planet.SATURN,
    ],

    Planet.SATURN: [
        Planet.MERCURY,
        Planet.VENUS,
    ],

    Planet.RAHU: [
        Planet.MERCURY,
        Planet.VENUS,
        Planet.SATURN,
    ],

    Planet.KETU: [
        Planet.MERCURY,
        Planet.VENUS,
        Planet.SATURN,
    ],
}


# ---------------------------------------------------------
# Enemies
# ---------------------------------------------------------

ENEMIES = {

    Planet.SUN: [
        Planet.VENUS,
        Planet.SATURN,
    ],

    Planet.MOON: [],

    Planet.MARS: [],

    Planet.MERCURY: [
        Planet.MOON,
        Planet.JUPITER,
    ],

    Planet.JUPITER: [
        Planet.VENUS,
        Planet.MERCURY,
    ],

    Planet.VENUS: [
        Planet.SUN,
        Planet.MOON,
    ],

    Planet.SATURN: [
        Planet.SUN,
        Planet.MARS,
        Planet.MOON,
    ],

    Planet.RAHU: [
        Planet.SUN,
        Planet.MOON,
        Planet.JUPITER,
    ],

    Planet.KETU: [
        Planet.SUN,
        Planet.MOON,
        Planet.JUPITER,
    ],
}


# ---------------------------------------------------------
# Neutral
# ---------------------------------------------------------

NEUTRAL = {

    Planet.SUN: [
        Planet.MERCURY,
    ],

    Planet.MOON: [
        Planet.MERCURY,
        Planet.VENUS,
        Planet.SATURN,
    ],

    Planet.MARS: [
        Planet.MERCURY,
        Planet.VENUS,
        Planet.SATURN,
    ],

    Planet.MERCURY: [
        Planet.SUN,
        Planet.MARS,
    ],

    Planet.JUPITER: [
        Planet.SATURN,
    ],

    Planet.VENUS: [
        Planet.MARS,
        Planet.JUPITER,
    ],

    Planet.SATURN: [
        Planet.JUPITER,
    ],

    Planet.RAHU: [
        Planet.MARS,
    ],

    Planet.KETU: [
        Planet.MARS,
    ],
}