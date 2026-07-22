"""
Instrument Domain Model

Represents a tradable instrument independent of any broker.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Instrument:
    """
    Broker-independent representation of a market instrument.
    """

    token: int
    symbol: str
    name: str
    exchange: str
    segment: str

    @property
    def is_index(self) -> bool:
        """
        Returns True if the instrument is an index.
        """
        return self.segment.upper() == "INDICES"

    @property
    def is_equity(self) -> bool:
        """
        Returns True if the instrument is an NSE/BSE equity.
        """
        return self.segment.upper() in {"NSE", "BSE"}

    def __str__(self) -> str:
        return (
            f"{self.symbol} "
            f"({self.exchange}) "
            f"[{self.token}]"
        )