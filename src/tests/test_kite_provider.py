"""
Test the Kite connection before downloading historical data.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from src.market.kite_service import KiteService
from src.market.providers.kite_provider import KiteProvider
from src.market.timeframe import Timeframe


def main():

    print("=" * 70)
    print("KITE CONNECTION TEST")
    print("=" * 70)

    service = KiteService()

    if not service.is_connected():
        print("\n❌ Kite authentication FAILED")
        print("Your access token has most likely expired.")
        return

    print("\n✅ Kite authentication successful")

    provider = KiteProvider()

    dataset = provider.download(
        symbol="NIFTY",
        timeframe=Timeframe.HOUR_1,
        start=datetime(2025, 1, 1, tzinfo=ZoneInfo("Asia/Kolkata")),
        end=datetime(2025, 1, 10, tzinfo=ZoneInfo("Asia/Kolkata")),
    )

    print(f"\nDownloaded {len(dataset)} bars")

    if len(dataset):
        print("\nFirst Bar")
        print(dataset.first())

        print("\nLast Bar")
        print(dataset.last())


if __name__ == "__main__":
    main()