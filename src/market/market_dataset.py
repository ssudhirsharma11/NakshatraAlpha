"""
Market Dataset

Represents a collection of OHLCV bars.
"""

from dataclasses import dataclass, field
from datetime import datetime

from src.market.ohlcv_bar import OHLCVBar


@dataclass
class MarketDataset:

    bars: list[OHLCVBar] = field(default_factory=list)

    def add(self, bar: OHLCVBar) -> None:
        self.bars.append(bar)

    def __len__(self) -> int:
        return len(self.bars)

    def __iter__(self):
        return iter(self.bars)

    def first(self) -> OHLCVBar | None:
        if not self.bars:
            return None
        return self.bars[0]

    def last(self) -> OHLCVBar | None:
        if not self.bars:
            return None
        return self.bars[-1]

    def between(
        self,
        start: datetime,
        end: datetime,
    ) -> list[OHLCVBar]:

        return [
            bar
            for bar in self.bars
            if start <= bar.timestamp <= end
        ]