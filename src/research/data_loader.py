from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
}


class DataLoader:
    """Loads historical OHLC data."""

    @staticmethod
    def load(path: str | Path) -> pd.DataFrame:

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        if path.suffix.lower() == ".csv":
            df = pd.read_csv(path)

        elif path.suffix.lower() == ".parquet":
            df = pd.read_parquet(path)

        else:
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        missing = REQUIRED_COLUMNS - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing required columns: {sorted(missing)}"
            )

        df["date"] = pd.to_datetime(df["date"])

        df = df.sort_values("date")

        df = df.reset_index(drop=True)

        return df