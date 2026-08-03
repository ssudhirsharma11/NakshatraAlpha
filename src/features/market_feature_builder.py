"""
Market Feature Builder

Calculates all derived market statistics
from a single OHLC candle.
"""

from __future__ import annotations

from src.models.market_features import (
    MarketFeatures,
)


class MarketFeatureBuilder:

    """
    Stateless market feature calculator.
    """

    @staticmethod
    def build(

        open_price: float,

        high_price: float,

        low_price: float,

        close_price: float,

        median_range_pct: float | None = None,

    ) -> MarketFeatures:

        # -----------------------------------------
        # Absolute values
        # -----------------------------------------

        body = abs(close_price - open_price)

        trading_range = high_price - low_price

        upper_wick = (
            high_price
            - max(open_price, close_price)
        )

        lower_wick = (
            min(open_price, close_price)
            - low_price
        )

        # -----------------------------------------
        # Percentages
        # -----------------------------------------

        return_pct = (
            (close_price - open_price)
            / open_price
        ) * 100

        range_pct = (
            trading_range
            / open_price
        ) * 100

        if trading_range == 0:

            body_pct = 0

            upper_wick_pct = 0

            lower_wick_pct = 0

            close_position_pct = 50

            open_position_pct = 50

        else:

            body_pct = (
                body
                / trading_range
            ) * 100

            upper_wick_pct = (
                upper_wick
                / trading_range
            ) * 100

            lower_wick_pct = (
                lower_wick
                / trading_range
            ) * 100

            close_position_pct = (
                (close_price - low_price)
                / trading_range
            ) * 100

            open_position_pct = (
                (open_price - low_price)
                / trading_range
            ) * 100

        # -----------------------------------------
        # Direction
        # -----------------------------------------

        if close_price > open_price:

            direction = "Bullish"

        elif close_price < open_price:

            direction = "Bearish"

        else:

            direction = "Neutral"

        # -----------------------------------------
        # Strength
        # -----------------------------------------

        if return_pct >= 0.50:

            strength = "Strong Bull"

        elif return_pct >= 0.20:

            strength = "Bull"

        elif return_pct <= -0.50:

            strength = "Strong Bear"

        elif return_pct <= -0.20:

            strength = "Bear"

        else:

            strength = "Neutral"

        # -----------------------------------------
        # Volatility
        # -----------------------------------------

        if median_range_pct is None:

            high_volatility = False

            low_volatility = False

        else:

            high_volatility = (
                range_pct >= median_range_pct
            )

            low_volatility = (
                range_pct < median_range_pct
            )

        return MarketFeatures(

            open=open_price,

            high=high_price,

            low=low_price,

            close=close_price,

            body=body,

            trading_range=trading_range,

            upper_wick=upper_wick,

            lower_wick=lower_wick,

            return_pct=return_pct,

            range_pct=range_pct,

            body_pct=body_pct,

            upper_wick_pct=upper_wick_pct,

            lower_wick_pct=lower_wick_pct,

            close_position_pct=close_position_pct,

            open_position_pct=open_position_pct,

            direction=direction,

            strength=strength,

            high_volatility=high_volatility,

            low_volatility=low_volatility,

        )