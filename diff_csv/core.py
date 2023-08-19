import diff_csv.utils
import csv


def read_file_raw(fname):
    """Read a CSV file, just line by line. Headers will be in the first row."""
    with open(fname, "r") as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]


def headers_match(h1, h2) -> bool:
    """Return if headers match. Headers h1 and h2 are passed as a list of header names."""
    pass
