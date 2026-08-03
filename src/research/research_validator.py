"""
Research Validator

Compares stored research values against
freshly calculated values.

This class contains no printing logic.
It simply returns validation results.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import isclose
from typing import Any


# ==========================================================
# FIELD RESULT
# ==========================================================

@dataclass(slots=True)
class FieldValidation:

    field: str

    stored: Any

    calculated: Any

    passed: bool

    reason: str = ""


# ==========================================================
# VALIDATION SUMMARY
# ==========================================================

@dataclass(slots=True)
class ValidationResult:

    date: str

    total_fields: int = 0

    passed_fields: int = 0

    failed_fields: int = 0

    fields: list[FieldValidation] = field(
        default_factory=list
    )

    @property
    def success(self) -> bool:

        return self.failed_fields == 0


# ==========================================================
# RESEARCH VALIDATOR
# ==========================================================

class ResearchValidator:
    """
    Compares two records field by field.
    """

    FLOAT_TOLERANCE = 1e-6

    IGNORE_FIELDS = {
        "chart",
    }

    # ------------------------------------------------------
    # Helpers
    # ------------------------------------------------------

    def _normalise(
        self,
        value: Any,
    ) -> Any:

        if hasattr(value, "value"):
            return value.value

        if hasattr(value, "name"):
            return value.name

        return value

    def _compare(
        self,
        stored: Any,
        calculated: Any,
    ) -> bool:

        stored = self._normalise(stored)
        calculated = self._normalise(calculated)

        if isinstance(stored, float) or isinstance(
            calculated,
            float,
        ):

            return isclose(
                float(stored),
                float(calculated),
                abs_tol=self.FLOAT_TOLERANCE,
            )

        return stored == calculated

    # ------------------------------------------------------
    # Main Validation
    # ------------------------------------------------------

    def validate(
        self,
        stored: dict,
        calculated: dict,
        date: str,
    ) -> ValidationResult:

        result = ValidationResult(
            date=date,
        )

        fields = sorted(

            set(stored.keys())
            &
            set(calculated.keys())

        )

        for field in fields:

            if field in self.IGNORE_FIELDS:
                continue

            stored_value = stored.get(field)

            calculated_value = calculated.get(field)

            passed = self._compare(
                stored_value,
                calculated_value,
            )

            validation = FieldValidation(

                field=field,

                stored=self._normalise(
                    stored_value,
                ),

                calculated=self._normalise(
                    calculated_value,
                ),

                passed=passed,

                reason="" if passed else "Values differ",

            )

            result.fields.append(
                validation
            )

        result.total_fields = len(
            result.fields
        )

        result.passed_fields = sum(

            f.passed

            for f in result.fields

        )

        result.failed_fields = (

            result.total_fields
            -
            result.passed_fields

        )

        return result