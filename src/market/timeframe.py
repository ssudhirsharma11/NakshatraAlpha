"""
Supported market timeframes.
"""

from enum import Enum


class Timeframe(Enum):
    MINUTE_1 = "1m"
    MINUTE_5 = "5m"
    MINUTE_15 = "15m"
    MINUTE_30 = "30m"

    HOUR_1 = "1h"
    HOUR_4 = "4h"

    DAILY = "1d"
    WEEKLY = "1w"
    MONTHLY = "1M"