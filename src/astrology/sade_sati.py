"""
Sade Sati Engine

Determines whether Saturn is in Sade Sati
based on its position from the Moon.

Distance Meaning

12 -> Rising Phase
1  -> Peak Phase
2  -> Setting Phase
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SadeSatiResult:
    """
    Result of Sade Sati calculation.
    """

    active: bool
    phase: str | None


class SadeSatiEngine:
    """
    Calculates Sade Sati status.
    """

    @staticmethod
    def calculate(
        saturn_from_moon: int,
    ) -> SadeSatiResult:

        if saturn_from_moon == 12:

            return SadeSatiResult(
                active=True,
                phase="Rising",
            )

        if saturn_from_moon == 1:

            return SadeSatiResult(
                active=True,
                phase="Peak",
            )

        if saturn_from_moon == 2:

            return SadeSatiResult(
                active=True,
                phase="Setting",
            )

        return SadeSatiResult(
            active=False,
            phase=None,
        )