"""
Market Universe

Single source of truth for all supported market indices.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.market.timeframe import Timeframe


# ==========================================================
# Historical Availability
# ==========================================================

DAILY_HISTORY_START = date(
    2000,
    1,
    1,
)

INTRADAY_HISTORY_START = date(
    2015,
    1,
    1,
)


# ==========================================================
# Market Definition
# ==========================================================

@dataclass(frozen=True)
class MarketDefinition:

    symbol: str

    category: str

    tier: int

    research_tags: tuple[str, ...]

    daily_start: date = DAILY_HISTORY_START

    intraday_start: date = INTRADAY_HISTORY_START

    def history_start(
        self,
        timeframe: Timeframe,
    ) -> date:

        if timeframe == Timeframe.DAILY:
            return self.daily_start

        return self.intraday_start


# ==========================================================
# Market Universe
# ==========================================================

MARKET_UNIVERSE = [

    # ======================================================
    # Broad Market
    # ======================================================

    MarketDefinition(

        symbol="NIFTY 50",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Benchmark",
            "Macro",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY NEXT 50",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Large Cap",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY 100",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Large Cap",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY 200",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Broad Market",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY 500",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Entire Market",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY TOTAL MKT",

        category="Broad Market",

        tier=1,

        research_tags=(
            "Entire Market",
        ),
    ),

    # ======================================================
    # Financial & Volatility
    # ======================================================

    MarketDefinition(

        symbol="NIFTY BANK",

        category="Financial",

        tier=1,

        research_tags=(
            "Jupiter",
            "Finance",
        ),
    ),

    MarketDefinition(

        symbol="INDIA VIX",

        category="Volatility",

        tier=1,

        research_tags=(
            "Fear",
            "Volatility",
        ),
    ),

    # ======================================================
    # Sector Indices
    # ======================================================

    MarketDefinition(

        symbol="NIFTY IT",

        category="Sector",

        tier=1,

        research_tags=(
            "Mercury",
            "Technology",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY METAL",

        category="Sector",

        tier=1,

        research_tags=(
            "Saturn",
            "Metals",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY AUTO",

        category="Sector",

        tier=1,

        research_tags=(
            "Mars",
            "Automobile",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY PHARMA",

        category="Sector",

        tier=1,

        research_tags=(
            "Health",
            "Medicine",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY FMCG",

        category="Sector",

        tier=1,

        research_tags=(
            "Venus",
            "Consumption",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY ENERGY",

        category="Sector",

        tier=1,

        research_tags=(
            "Energy",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY OIL AND GAS",

        category="Sector",

        tier=1,

        research_tags=(
            "Saturn",
            "Oil",
            "Gas",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY REALTY",

        category="Sector",

        tier=1,

        research_tags=(
            "Real Estate",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY INFRA",

        category="Sector",

        tier=1,

        research_tags=(
            "Infrastructure",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY HEALTHCARE",

        category="Sector",

        tier=1,

        research_tags=(
            "Healthcare",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY CONSUMPTION",

        category="Sector",

        tier=1,

        research_tags=(
            "Consumption",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY COMMODITIES",

        category="Sector",

        tier=1,

        research_tags=(
            "Commodities",
        ),
    ),

    MarketDefinition(

        symbol="NIFTY SERV SECTOR",

        category="Sector",

        tier=1,

        research_tags=(
            "Services",
        ),
    ),

]


# ==========================================================
# Convenience Functions
# ==========================================================

def get_market(
    symbol: str,
) -> MarketDefinition:
    """
    Returns MarketDefinition for a symbol.
    """

    for market in MARKET_UNIVERSE:

        if market.symbol.upper() == symbol.upper():

            return market

    raise ValueError(
        f"Unknown market: {symbol}"
    )


def tier_markets(
    tier: int,
) -> list[MarketDefinition]:
    """
    Returns all markets belonging to a tier.
    """

    return [

        market

        for market in MARKET_UNIVERSE

        if market.tier == tier

    ]


def markets_by_category(
    category: str,
) -> list[MarketDefinition]:
    """
    Returns all markets in a category.
    """

    return [

        market

        for market in MARKET_UNIVERSE

        if market.category.lower() == category.lower()

    ]


def markets_by_tag(
    tag: str,
) -> list[MarketDefinition]:
    """
    Returns all markets matching a research tag.
    """

    tag = tag.lower()

    return [

        market

        for market in MARKET_UNIVERSE

        if any(
            t.lower() == tag
            for t in market.research_tags
        )

    ]