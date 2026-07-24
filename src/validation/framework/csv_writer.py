"""
Reusable CSV Writer
"""

import csv


class CsvWriter:

    @staticmethod
    def write(path, header, rows):

        with open(
            path,
            "w",
            newline="",
        ) as f:

            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerows(rows)