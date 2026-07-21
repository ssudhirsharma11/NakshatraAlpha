"""
Sprint 20B - Historical Data Service

Downloads historical OHLC data from Zerodha
and saves it as CSV.
"""

from pathlib import Path

import pandas as pd

from src.market.kite_service import KiteService


class HistoricalDataService:

    def __init__(self):
        self.kite = KiteService().connect()

    def download_history(
        self,
        instrument_token: int,
        from_date: str,
        to_date: str,
        interval: str = "5minute",
    ) -> pd.DataFrame:

        print("\nDownloading historical data...\n")

        data = self.kite.historical_data(
            instrument_token=instrument_token,
            from_date=from_date,
            to_date=to_date,
            interval=interval,
            continuous=False,
            oi=False,
        )

        df = pd.DataFrame(data)

        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)

        filename = (
            f"{instrument_token}_{interval}_"
            f"{from_date.replace('-', '')}_"
            f"{to_date.replace('-', '')}.csv"
        )

        file_path = output_dir / filename

        df.to_csv(file_path, index=False)

        print(f"✅ Downloaded {len(df)} candles")
        print(f"✅ Saved to {file_path}")

        return df