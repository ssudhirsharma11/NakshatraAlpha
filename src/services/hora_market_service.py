"""
Hora Market Service

Builds aggregated market statistics for one Hora or
for any supplied interval within a Hora.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from src.models.hora import Hora
from src.models.market_snapshot import MarketSnapshot
from src.services.market_data_service import MarketDataService


@dataclass(slots=True, frozen=True)
class HoraMarketResult:
    """
    Complete market result for one Hora.
    """

    hora: Hora

    market: MarketSnapshot


class HoraMarketService:
    """
    Computes aggregated market statistics.
    """

    def __init__(
        self,
        market_data_service: MarketDataService | None = None,
    ):
        self.market_data_service = (
            market_data_service
            or MarketDataService()
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def build(
        self,
        hora: Hora,
    ) -> HoraMarketResult:
        """
        Uses the full Hora interval.
        """

        return self.build_between(
            hora=hora,
            start=hora.start,
            end=hora.end,
        )

    def build_between(
        self,
        hora: Hora,
        start: datetime,
        end: datetime,
    ) -> HoraMarketResult:
        """
        Aggregates market data between the supplied timestamps.

        The Hora identity is preserved while allowing the
        analysed market interval to be shorter than the Hora.
        """

        candles = self.market_data_service.get_between(
            start=start,
            end=end,
        )

        if candles.empty:
            raise ValueError(
                f"No market candles found between "
                f"{start} and {end}"
            )

        open_price = float(
            candles.iloc[0]["open"]
        )

        high_price = float(
            candles["high"].max()
        )

        low_price = float(
            candles["low"].min()
        )

        close_price = float(
            candles.iloc[-1]["close"]
        )

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