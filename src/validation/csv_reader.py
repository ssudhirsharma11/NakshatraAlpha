"""
Reusable CSV Reader
"""

import csv


class CsvReader:

    @staticmethod
    def read(path):

        with open(
            path,
            newline="",
        ) as f:

            return list(csv.DictReader(f))