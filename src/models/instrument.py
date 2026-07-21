"""
Sprint 20B - Instrument Service

Downloads the complete NSE instrument master from Zerodha
and saves it locally for historical data lookups.
"""

import os
import pandas as pd

from dotenv import load_dotenv
from kiteconnect import KiteConnect

load_dotenv()

API_KEY = os.getenv("KITE_API_KEY")
API_SECRET = os.getenv("KITE_API_SECRET")


class InstrumentService:

    def __init__(self):

        if not API_KEY:
            raise ValueError("KITE_API_KEY not found.")

        self.kite = KiteConnect(api_key=API_KEY)

    def set_access_token(self, access_token: str):

        self.kite.set_access_token(access_token)

    def download_instruments(self, exchange="NSE"):

        print(f"Downloading {exchange} instruments...")

        instruments = self.kite.instruments(exchange)

        df = pd.DataFrame(instruments)

        os.makedirs("data/raw", exist_ok=True)

        file_path = f"data/raw/{exchange.lower()}_instruments.csv"

        df.to_csv(file_path, index=False)

        print(f"Saved {len(df)} instruments.")

        print(f"Location: {file_path}")

        return df

    def find_symbol(self, df, symbol):

        result = df[df["tradingsymbol"] == symbol]

        return result