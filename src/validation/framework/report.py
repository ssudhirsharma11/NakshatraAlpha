"""
Validation Report
"""

from dataclasses import dataclass


@dataclass
class ValidationReport:
    module: str
    total: int = 0
    passed: int = 0
    failed: int = 0

    @property
    def accuracy(self) -> float:
        if self.total == 0:
            return 0.0
        return (self.passed / self.total) * 100

    def print(self):

        print()
        print("=" * 65)
        print(f"Module    : {self.module}")
        print(f"Tests     : {self.total}")
        print(f"Passed    : {self.passed}")
        print(f"Failed    : {self.failed}")
        print(f"Accuracy  : {self.accuracy:.2f}%")

        if self.failed == 0:
            print("\nPASS")
        else:
            print("\nFAIL")

        print("=" * 65)