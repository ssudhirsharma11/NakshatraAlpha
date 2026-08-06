"""
List Available NSE Indices

Prints every NSE index available from Kite.
"""

from kiteconnect import KiteConnect

from src.market.kite_service import KiteService


def main():

    kite: KiteConnect = KiteService().get_client()

    print("\nFetching instruments...")

    instruments = kite.instruments()

    print()

    print("=" * 80)
    print("AVAILABLE NSE INDICES")
    print("=" * 80)

    count = 0

    for instrument in instruments:

        if instrument["exchange"] != "NSE":
            continue

        if instrument["segment"] != "INDICES":
            continue

        count += 1

        print(
            f"{count:3d}. "
            f"{instrument['tradingsymbol']}"
        )

    print()

    print("=" * 80)
    print(f"Total Indices : {count}")
    print("=" * 80)


if __name__ == "__main__":
    main()