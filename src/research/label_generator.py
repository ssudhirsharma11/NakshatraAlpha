from __future__ import annotations

import pandas as pd


class LabelGenerator:

    @staticmethod
    def generate(df: pd.DataFrame) -> pd.DataFrame:

        close = df["close"]

        df["future_return_1"] = (
            close.shift(-1) - close
        ) / close

        df["future_return_3"] = (
            close.shift(-3) - close
        ) / close

        df["future_return_6"] = (
            close.shift(-6) - close
        ) / close

        df["future_return_12"] = (
            close.shift(-12) - close
        ) / close

        return df