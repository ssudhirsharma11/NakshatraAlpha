"""
Golden regression test for Tithi.
"""

import csv
from datetime import datetime

from src.services.chart_builder import ChartBuilder
from src.astrology.tithi import TithiEngine


LATITUDE = 28.6139
LONGITUDE = 77.2090


def main():

    failures = 0
    total = 0

    with open(
        "src/validation/tithi/tithi_golden.csv",
        newline="",
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            total += 1

            timestamp = datetime.fromisoformat(
                row["timestamp"]
            )

            chart = ChartBuilder.build(
                timestamp,
                LATITUDE,
                LONGITUDE,
            )

            result = TithiEngine.calculate(chart)

            expected = int(row["tithi_number"])

            if result.number != expected:

                failures += 1

                print(
                    f"FAILED {timestamp} "
                    f"Expected={expected} "
                    f"Got={result.number}"
                )

    print()
    print("=" * 60)
    print(f"Total Tests : {total}")
    print(f"Failures    : {failures}")

    if failures == 0:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    main()