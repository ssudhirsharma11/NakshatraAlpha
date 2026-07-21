from src.market.data_validator import DataValidator


def main():

    validator = DataValidator(
        "data/raw/256265_5minute_20260427_20260717.csv"
    )

    validator.validate()


if __name__ == "__main__":
    main()