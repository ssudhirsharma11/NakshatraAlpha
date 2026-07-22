from datetime import datetime
from zoneinfo import ZoneInfo

from src.market.ohlcv_bar import OHLCVBar
from src.market.timeframe import Timeframe


def main():

    bar = OHLCVBar(

        symbol="NIFTY",

        timeframe=Timeframe.HOUR_1,

        timestamp=datetime(
            2026,
            7,
            14,
            10,
            0,
            tzinfo=ZoneInfo("Asia/Kolkata"),
        ),

        open=25100.50,

        high=25182.10,

        low=25088.40,

        close=25160.25,

        volume=1289456,
    )

    print()

    print("=" * 60)

    print("OHLCV BAR")

    print("=" * 60)

    print(bar)


if __name__ == "__main__":
    main()