"""
Feature Set

Holds all derived astrological features for a single timestamp.
This object is intentionally independent of market data and is later
combined with OHLC candles to create the master research dataset.
"""

from dataclasses import dataclass
from typing import Optional

from src.models.chart import Chart
from src.models.hora import Hora
from src.models.nakshatra_enum import NakshatraEnum
from src.models.paksha import Paksha
from src.models.planet import Planet
from src.models.sign import Sign
from src.models.tithi_enum import TithiEnum


@dataclass(slots=True)
class FeatureSet:
    """
    Complete feature set for one timestamp.
    """

    # ------------------------------------------------------------------
    # Source
    # ------------------------------------------------------------------

    chart: Chart

    # ------------------------------------------------------------------
    # Calendar
    # ------------------------------------------------------------------

    weekday: Optional[int] = None

    # ------------------------------------------------------------------
    # Hora
    # ------------------------------------------------------------------

    hora_number: Optional[int] = None
    hora: Optional[Hora] = None
    hora_lord: Optional[Planet] = None

    # ------------------------------------------------------------------
    # Tithi
    # ------------------------------------------------------------------

    tithi: Optional[TithiEnum] = None
    tithi_number: Optional[int] = None
    paksha: Optional[Paksha] = None

    # ------------------------------------------------------------------
    # Nakshatra
    # ------------------------------------------------------------------

    moon_nakshatra: Optional[NakshatraEnum] = None
    moon_nakshatra_number: Optional[int] = None

    sun_nakshatra: Optional[NakshatraEnum] = None
    sun_nakshatra_number: Optional[int] = None

    pada: Optional[int] = None

    # ------------------------------------------------------------------
    # Lagna
    # ------------------------------------------------------------------

    lagna_sign: Optional[Sign] = None
    lagna_number: Optional[int] = None
    lagna_degree: Optional[float] = None

    # ------------------------------------------------------------------
    # Planet Positions
    # ------------------------------------------------------------------

    sun_longitude: Optional[float] = None
    moon_longitude: Optional[float] = None

    sun_sign: Optional[Sign] = None
    sun_sign_number: Optional[int] = None

    moon_sign: Optional[Sign] = None
    moon_sign_number: Optional[int] = None

    sun_navamsha: Optional[Sign] = None
    moon_navamsha: Optional[Sign] = None

    saturn_sign: Optional[Sign] = None

    # ------------------------------------------------------------------
    # Relationships
    # ------------------------------------------------------------------

    saturn_from_sun: Optional[int] = None
    saturn_kendra_from_sun: Optional[bool] = None

    saturn_from_moon: Optional[int] = None

    # ------------------------------------------------------------------
    # Sade Sati
    # ------------------------------------------------------------------

    sade_sati: Optional[bool] = None

    # Rising / Peak / Setting
    sade_sati_phase: Optional[str] = None