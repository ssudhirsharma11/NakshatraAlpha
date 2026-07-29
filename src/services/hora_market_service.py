"""
Hora Market Service

Builds market statistics for a single Hora.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.models.hora import Hora
from src.models.market_snapshot import MarketSnapshot
from src.services.market_data_service import MarketDataService


@dataclass(slots=True, frozen=True)
class HoraMarketResult:
    """
    Complete market result for one Hora.

    Combines the Hora object with the aggregated
    market statistics.
    """

    hora: Hora
    market: MarketSnapshot


class HoraMarketService:
    """
    Computes market statistics for a Hora.
    """

    def __init__(
        self,
        market_data_service: MarketDataService | None = None,
    ):
        self.market_data_service = (
            market_data_service
            or MarketDataService()
        )

    def build(
        self,
        hora: Hora,
    ) -> HoraMarketResult:
        """
        Build market statistics for one Hora.

        Parameters
        ----------
        hora
            Hora whose market behaviour is required.

        Returns
        -------
        HoraMarketResult
        """

        candles = self.market_data_service.get_between(
            start=hora.start,
            end=hora.end,
        )

        if candles.empty:
            raise ValueError(
                f"No market candles found between "
                f"{hora.start} and {hora.end}"
            )

        open_price = float(candles.iloc[0]["open"])
        high_price = float(candles["high"].max())
        low_price = float(candles["low"].min())
        close_price = float(candles.iloc[-1]["close"])

        snapshot = MarketSnapshot(
            open=open_price,
            high=high_price,
            low=low_price,
            close=close_price,
            up_move=high_price - open_price,
            down_move=open_price - low_price,
            trading_range=high_price - low_price,
            candle_count=len(candles),
        )

        return HoraMarketResult(
            hora=hora,
            market=snapshot,
        )