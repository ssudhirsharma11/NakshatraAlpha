"""
Validation Runner

Runs validation cases against the complete
Feature Builder pipeline.
"""

from __future__ import annotations

from pathlib import Path

from src.features.feature_builder import FeatureBuilder
from src.services.chart_builder import ChartBuilder
from src.validation.validation_loader import ValidationLoader


class ValidationRunner:
    """
    Runs validation cases.
    """

    @staticmethod
    def _compare(
        label: str,
        expected,
        actual,
    ) -> bool:

        if expected is None:
            return True

        passed = expected == actual

        print(
            f"{label:<22}"
            f"Expected : {expected}"
        )

        print(
            f"{'':<22}"
            f"Actual   : {actual}"
        )

        print(
            f"{'':<22}"
            f"{'PASS' if passed else 'FAIL'}"
        )

        print()

        return passed

    @staticmethod
    def run(
        csv_path: str | Path,
    ):

        cases = ValidationLoader.load(csv_path)

        feature_builder = FeatureBuilder()

        total_cases = 0

        passed_fields = {}

        print("=" * 80)
        print("NAKSHATRA ALPHA VALIDATION")
        print("=" * 80)

        for case in cases:

            total_cases += 1

            chart = ChartBuilder.build(
                timestamp=case.timestamp,
                latitude=case.latitude,
                longitude=case.longitude,
            )

            features = feature_builder.build(chart)

            print()
            print("=" * 80)

            print(
                f"CASE {total_cases}"
            )

            print("=" * 80)

            print(
                f"Timestamp : {case.timestamp}"
            )

            print()

            checks = [

                (
                    "Weekday",
                    case.expected_weekday,
                    chart.timestamp.strftime("%A"),
                ),

                (
                    "Tithi",
                    case.expected_tithi,
                    features.tithi.name,
                ),

                (
                    "Tithi Group",
                    case.expected_tithi_group,
                    (
                        features.tithi_group.name
                        if features.tithi_group
                        else None
                    ),
                ),

                (
                    "Tithi Lord",
                    case.expected_tithi_lord,
                    (
                        features.tithi_lord.name
                        if features.tithi_lord
                        else None
                    ),
                ),

                (
                    "Paksha",
                    case.expected_paksha,
                    (
                        features.paksha.name
                        if features.paksha
                        else None
                    ),
                ),

                (
                    "Moon Nakshatra",
                    case.expected_moon_nakshatra,
                    (
                        features.moon_nakshatra.name
                        if features.moon_nakshatra
                        else None
                    ),
                ),

                (
                    "Pada",
                    case.expected_pada,
                    features.pada,
                ),

                (
                    "Sun Sign",
                    case.expected_sun_sign,
                    (
                        features.sun_sign.name
                        if features.sun_sign
                        else None
                    ),
                ),

                (
                    "Moon Sign",
                    case.expected_moon_sign,
                    (
                        features.moon_sign.name
                        if features.moon_sign
                        else None
                    ),
                ),

                (
                    "Lagna",
                    case.expected_lagna,
                    (
                        features.lagna_sign.name
                        if features.lagna_sign
                        else None
                    ),
                ),

                (
                    "Saturn From Sun",
                    case.expected_saturn_from_sun,
                    features.saturn_from_sun,
                ),

                (
                    "Saturn From Moon",
                    case.expected_saturn_from_moon,
                    features.saturn_from_moon,
                ),

                (
                    "Sade Sati",
                    case.expected_sade_sati,
                    features.sade_sati,
                ),

                (
                    "Sade Sati Phase",
                    case.expected_sade_sati_phase,
                    features.sade_sati_phase,
                ),

            ]

            for label, expected, actual in checks:

                if expected is None:
                    continue

                passed = ValidationRunner._compare(
                    label,
                    expected,
                    actual,
                )

                if label not in passed_fields:
                    passed_fields[label] = 0

                if passed:
                    passed_fields[label] += 1

        print()
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)

        print(
            f"Cases Tested : {total_cases}"
        )

        print()

        for field in sorted(
            passed_fields.keys()
        ):

            print(
                f"{field:<22}"
                f"{passed_fields[field]}/{total_cases}"
            )

        print()
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