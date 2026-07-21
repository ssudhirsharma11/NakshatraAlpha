from src.market.instrument_service import InstrumentService

import pandas as pd


def main():

    service = InstrumentService()

    df = pd.read_csv("data/raw/nse_instruments.csv")

    # Show all rows containing the word NIFTY
    result = df[df["tradingsymbol"].str.contains("NIFTY", case=False, na=False)]

    print(result)


if __name__ == "__main__":
    main()