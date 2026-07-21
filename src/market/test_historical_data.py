from src.market.historical_data_service import HistoricalDataService


def main():

    service = HistoricalDataService()

    df = service.download_history(
        instrument_token=256265,
        from_date="2026-04-27",
        to_date="2026-07-17",
        interval="5minute",
    )

    print(df.head())

    print(df.tail())


if __name__ == "__main__":
    main()