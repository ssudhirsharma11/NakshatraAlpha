"""
Kite Connect market provider.
"""

from datetime import datetime

from kiteconnect import KiteConnect

from src.market.kite_service import KiteService
from src.market.market_dataset import MarketDataset
from src.market.ohlcv_bar import OHLCVBar
from src.market.providers.base_provider import BaseMarketProvider
from src.market.timeframe import Timeframe


class KiteProvider(BaseMarketProvider):

    INDEX_ALIASES = {
        "NIFTY": "NIFTY 50",
        "BANKNIFTY": "NIFTY BANK",
        "FINNIFTY": "NIFTY FINANCIAL SERVICES",
        "MIDCPNIFTY": "NIFTY MIDCAP SELECT",
    }

    def __init__(self):
        self.kite: KiteConnect = KiteService().connect()

    def download(
        self,
        symbol: str,
        timeframe: Timeframe,
        start: datetime,
        end: datetime,
    ) -> MarketDataset:

        dataset = MarketDataset()

        instrument = self._find_instrument(symbol)

        if instrument is None:
            raise ValueError(f"Instrument '{symbol}' not found.")

        candles = self.kite.historical_data(
            instrument_token=instrument["instrument_token"],
            from_date=start,
            to_date=end,
            interval=self._map_interval(timeframe),
            continuous=False,
            oi=False,
        )

        for candle in candles:

            dataset.add(
                OHLCVBar(
                    symbol=symbol,
                    timeframe=timeframe,
                    timestamp=candle["date"],
                    open=float(candle["open"]),
                    high=float(candle["high"]),
                    low=float(candle["low"]),
                    close=float(candle["close"]),
                    volume=float(candle["volume"]),
                )
            )

        return dataset

    def _find_instrument(self, symbol: str):

        search_symbol = self.INDEX_ALIASES.get(symbol.upper(), symbol).upper()

        print(f"\nSearching for: {search_symbol}")

        instruments = self.kite.instruments()

        for instrument in instruments:

            if (
                instrument["exchange"] == "NSE"
                and instrument["tradingsymbol"].upper() == search_symbol
            ):
                print(f"Found instrument: {instrument['tradingsymbol']}")
                return instrument

        return None

    @staticmethod
    def _map_interval(timeframe: Timeframe) -> str:

        mapping = {
            Timeframe.MINUTE_1: "minute",
            Timeframe.MINUTE_5: "5minute",
            Timeframe.MINUTE_15: "15minute",
            Timeframe.MINUTE_30: "30minute",
            Timeframe.HOUR_1: "60minute",
            Timeframe.DAILY: "day",
            Timeframe.WEEKLY: "week",
        }

        return mapping[timeframe]