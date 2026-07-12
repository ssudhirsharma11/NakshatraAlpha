"""
Nakshatra Model
"""

from dataclasses import dataclass


@dataclass
class Nakshatra:

    name: str
    number: int
    start_degree: float
    end_degree: float