"""
Sprint 20B - Instrument Service

Downloads and manages NSE instrument master.
"""

from pathlib import Path

import pandas as pd

from src.market.kite_service import KiteService


class InstrumentService:

    def __init__(self):
        self.kite = KiteService().connect()

    def download_instruments(self, exchange: str = "NSE") -> pd.DataFrame:
        """Download instrument master from Zerodha."""

        print(f"\nDownloading {exchange} instruments...\n")

        instruments = self.kite.instruments(exchange)

        df = pd.DataFrame(instruments)

        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{exchange.lower()}_instruments.csv"

        df.to_csv(output_file, index=False)

        print(f"✅ {len(df)} instruments downloaded.")
        print(f"✅ Saved to {output_file}")

        return df

    def find_by_symbol(self, symbol: str, exchange: str = "NSE") -> pd.DataFrame:
        """Find a symbol from downloaded instrument master."""

        file_path = Path("data/raw") / f"{exchange.lower()}_instruments.csv"

        if not file_path.exists():
            raise FileNotFoundError(
                "Instrument file not found. Please run download_instruments() first."
            )

        df = pd.read_csv(file_path)

        return df[df["tradingsymbol"] == symbol]