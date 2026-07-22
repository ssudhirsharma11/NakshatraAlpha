"""
Instrument Repository

Purpose
-------
Loads the Kite instrument master once and provides fast,
broker-independent instrument lookups.
"""

from __future__ import annotations

from typing import Dict

from kiteconnect import KiteConnect

from src.market.instrument import Instrument


class InstrumentRepository:
    """
    Repository providing cached instrument lookup.
    """

    _ALIASES = {
        "NIFTY": "NIFTY 50",
        "BANKNIFTY": "NIFTY BANK",
    }

    def __init__(self, kite: KiteConnect):

        self._kite = kite
        self._cache: Dict[str, Instrument] = {}
        self._loaded = False

    def _load(self):

        if self._loaded:
            return

        print("Loading instrument master...")

        for item in self._kite.instruments("NSE"):

            instrument = Instrument(
                token=item["instrument_token"],
                symbol=item["tradingsymbol"],
                name=item["name"],
                exchange=item["exchange"],
                segment=item["segment"],
            )

            self._cache[instrument.symbol.upper()] = instrument

        self._loaded = True

        print(f"Loaded {len(self._cache)} instruments.")

    def get(self, symbol: str) -> Instrument:

        self._load()

        lookup = self._ALIASES.get(
            symbol.upper(),
            symbol.upper(),
        )

        instrument = self._cache.get(lookup)

        if instrument is None:
            raise ValueError(
                f"Instrument '{symbol}' not found."
            )

        return instrument

    def token(self, symbol: str) -> int:
        return self.get(symbol).token