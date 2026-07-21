from src.astrology.zodiac import ZodiacEngine


def main():

    test_values = [
        0,
        15.25,
        29.99,
        30,
        45,
        89,
        121.75,
        180,
        270,
        341.2,
        359.99,
    ]

    print()

    print("=" * 65)
    print("              ZODIAC ENGINE TEST")
    print("=" * 65)

    for longitude in test_values:

        sign = ZodiacEngine.get_sign(longitude)

        print(
            f"{longitude:8.2f}°   "
            f"{sign.sign_name:<12}"
            f"{sign.degree_in_sign:6.2f}°"
        )

    print("=" * 65)


if __name__ == "__main__":
    main()