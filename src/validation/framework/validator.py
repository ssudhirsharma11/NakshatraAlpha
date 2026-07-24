"""
Generic Validator
"""

from src.validation.framework.report import ValidationReport


class Validator:

    def __init__(self, module):

        self.report = ValidationReport(module)

    def compare(self, expected, actual):

        self.report.total += 1

        if expected == actual:
            self.report.passed += 1
            return True

        self.report.failed += 1

        print(
            f"FAILED\n"
            f"Expected : {expected}\n"
            f"Actual   : {actual}\n"
        )

        return False

    def finish(self):

        self.report.print()