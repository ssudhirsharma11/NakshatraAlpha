"""
Validation Runner

Runs validation cases against the astrology engines.
"""

from pathlib import Path

from src.astrology.nakshatra import NakshatraEngine
from src.astrology.tithi import TithiEngine
from src.services.chart_builder import ChartBuilder
from src.validation.validation_loader import ValidationLoader
from src.models.planet import Planet


class ValidationRunner:
    """
    Runs validation cases.
    """

    @staticmethod
    def run(csv_path: str | Path):

        cases = ValidationLoader.load(csv_path)

        total_cases = 0

        tithi_pass = 0
        nakshatra_pass = 0

        print("=" * 80)
        print("VALIDATION REPORT")
        print("=" * 80)

        for case in cases:

            total_cases += 1

            chart = ChartBuilder.build(
                timestamp=case.timestamp,
                latitude=case.latitude,
                longitude=case.longitude,
            )

            tithi = TithiEngine.calculate(chart)

            moon_nakshatra = NakshatraEngine.calculate(
                chart,
                Planet.MOON,
            )

            print()

            print("-" * 80)

            print(f"Case #{total_cases}")

            print(f"Timestamp : {case.timestamp}")
            print(f"Latitude  : {case.latitude}")
            print(f"Longitude : {case.longitude}")

            print()

            if case.expected_tithi:

                passed = (
                    tithi.tithi.name ==
                    case.expected_tithi
                )

                if passed:
                    tithi_pass += 1

                print(
                    f"Tithi      Expected : {case.expected_tithi}"
                )

                print(
                    f"Tithi      Actual   : {tithi.tithi.name}"
                )

                print(
                    f"Status              : {'PASS' if passed else 'FAIL'}"
                )

                print()

            if case.expected_nakshatra:

                passed = (
                    moon_nakshatra.nakshatra.name ==
                    case.expected_nakshatra
                )

                if passed:
                    nakshatra_pass += 1

                print(
                    f"Nakshatra Expected : {case.expected_nakshatra}"
                )

                print(
                    f"Nakshatra Actual   : {moon_nakshatra.nakshatra.name}"
                )

                print(
                    f"Status             : {'PASS' if passed else 'FAIL'}"
                )

        print()

        print("=" * 80)

        print("SUMMARY")

        print("=" * 80)

        print(f"Cases Tested        : {total_cases}")

        print(
            f"Tithi Accuracy      : "
            f"{tithi_pass}/{total_cases}"
        )

        print(
            f"Nakshatra Accuracy  : "
            f"{nakshatra_pass}/{total_cases}"
        )

        if (
            tithi_pass == total_cases and
            nakshatra_pass == total_cases
        ):
            print("\nOVERALL RESULT : PASS")
        else:
            print("\nOVERALL RESULT : FAIL")

        print("=" * 80)


def main():

    csv_file = (
        Path(__file__).resolve().parents[1]
        / "tests"
        / "data"
        / "validation"
        / "tithi_validation.csv"
    )

    ValidationRunner.run(csv_file)


if __name__ == "__main__":
    main()