#!/usr/bin/env python3

"""
Script for processing an exported CSV from the "Combined" tab of the current
year's "Teams Organisation (internal)" spreadsheet for use in emailing teams.

Outputs to standard output, typical usage is to redirect that to a file.
"""

import argparse
import csv
import re
import sys
from typing import TextIO


def pascal_case(text: str) -> str:
    if text.isupper():
        return text
    return re.sub(r'\W+', '', text.title())


def main(input_csv: TextIO, in_place: bool) -> None:
    rows = list(csv.reader(input_csv))

    super_header_row = rows.pop(0)
    header_row = rows.pop(0)

    try:
        supervisor_offset = super_header_row.index('Supervisor')
        secondary_contact_offset = super_header_row.index('Secondary Contact')
        secondary_contact_end = super_header_row.index('Kit Info')
    except ValueError as e:
        raise ValueError(f"Badly formed input file: {e}") from e

    status_col = header_row.index('Status')

    # Update in place to ensure the new values are written back
    header_row = [pascal_case(x) for x in header_row]

    for idx, value in enumerate(header_row):
        if idx < supervisor_offset or idx > secondary_contact_end:
            continue
        if idx < secondary_contact_offset:
            header_row[idx] = 'Primary' + value
        else:
            header_row[idx] = 'Secondary' + value

    rows = [x for x in rows if x[status_col] not in ('Dropped Out', '')]

    if in_place:
        input_csv.seek(0)
        input_csv.truncate()
        output = input_csv
    else:
        output = sys.stdout

    csv.writer(output).writerow(header_row)
    csv.writer(output).writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'input_csv',
        help="CSV file to process",
        type=argparse.FileType(mode='r+'),
    )
    parser.add_argument(
        '--in-place',
        action='store_true',
        default=False,
        help="Update the file in place (discouraged)",
    )
    return parser.parse_args()


if __name__ == '__main__':
    main(**(parse_args().__dict__))
