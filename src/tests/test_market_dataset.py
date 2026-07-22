from datetime import datetime
from zoneinfo import ZoneInfo

from src.market.market_dataset import MarketDataset
from src.market.ohlcv_bar import OHLCVBar
from src.market.timeframe import Timeframe


def create_bar(hour, close):

    return OHLCVBar(
        symbol="NIFTY",

        timeframe=Timeframe.HOUR_1,

        timestamp=datetime(
            2026,
            7,
            14,
            hour,
            0,
            tzinfo=ZoneInfo("Asia/Kolkata"),
        ),

        open=25000,

        high=25100,

        low=24950,

        close=close,

        volume=100000,
    )


def main():

    dataset = MarketDataset()

    dataset.add(create_bar(9, 25025))
    dataset.add(create_bar(10, 25080))
    dataset.add(create_bar(11, 25120))

    print()

    print("=" * 60)
    print("MARKET DATASET")
    print("=" * 60)

    print("Bars :", len(dataset))

    print("First:", dataset.first())

    print("Last :", dataset.last())

    print()

    print("Iterating:")

    for bar in dataset:
        print(bar.timestamp, bar.close)


if __name__ == "__main__":
    main()