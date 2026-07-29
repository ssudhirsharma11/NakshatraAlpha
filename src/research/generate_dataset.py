"""
Generate Research Dataset

Creates:
1. raw_dataset.csv
2. research_dataset.csv
"""

from __future__ import annotations

from pathlib import Path

from src.research.dataset_builder import DatasetBuilder
from src.research.dataset_enricher import DatasetEnricher
from src.research.dataset_validator import DatasetValidator


def main() -> None:

    print("\n" + "=" * 70)
    print("NAKSHATRA ALPHA DATASET GENERATION")
    print("=" * 70)

    output_dir = Path("data/research")
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ----------------------------------------------------------
    # Build Raw Dataset
    # ----------------------------------------------------------

    print("\nBuilding raw dataset...\n")

    builder = DatasetBuilder()
    raw_df = builder.build()

    raw_file = output_dir / "raw_dataset.csv"

    raw_df.to_csv(
        raw_file,
        index=False,
    )

    print(f"✓ Raw dataset saved to {raw_file}")

    # ----------------------------------------------------------
    # Validate Raw Dataset
    # ----------------------------------------------------------

    print("\nValidating raw dataset...\n")

    validator = DatasetValidator()

    if not validator.validate(raw_file):
        raise RuntimeError(
            "Dataset validation failed. Research dataset not generated."
        )

    # ----------------------------------------------------------
    # Enrich Dataset
    # ----------------------------------------------------------

    print("\nEnriching dataset...\n")

    enricher = DatasetEnricher()

    research_df = enricher.enrich(raw_df)

    research_file = output_dir / "research_dataset.csv"

    research_df.to_csv(
        research_file,
        index=False,
    )

    print(f"✓ Research dataset saved to {research_file}")

    # ----------------------------------------------------------
    # Summary
    # ----------------------------------------------------------

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Raw Rows              : {len(raw_df):,}")
    print(f"Research Rows         : {len(research_df):,}")
    print(f"Research Columns      : {len(research_df.columns)}")

    print("\nDone.\n")


if __name__ == "__main__":
    main()