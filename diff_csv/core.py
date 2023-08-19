import diff_csv.utils
import csv


def file_to_dict(fname):
    """Read a csv file into a list of dictionaries, one dict per row."""
    rows = []
    with open(fname, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)

    return rows


def headers_match(h1, h2) -> bool:
    """Return if headers match. Headers h1 and h2 are passed as a list of header names."""
    pass
