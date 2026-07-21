"""
Market Loader

Loads validated historical market data for research.
"""

from pathlib import Path

import pandas as pd


class MarketLoader:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> pd.DataFrame:

        if not self.file_path.exists():
            raise FileNotFoundError(f"{self.file_path} not found.")

        df = pd.read_csv(self.file_path)

        df["date"] = pd.to_datetime(df["date"])

        return df