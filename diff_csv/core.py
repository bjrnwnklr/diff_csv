import diff_csv.utils
import csv
import logging


def read_file_raw(fname):
    """Read a CSV file, just line by line. Headers will be in the first row."""
    with open(fname, "r") as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]


def headers_match(f1, f2) -> bool:
    """Return if headers match. Headers are taken from the first row of the list if rows."""
    # check number of columns is the same
    h1 = f1[0]
    h2 = f2[0]
    if len(h1) != len(h2):
        logging.info(f"Headers have different number of fields: {len(h1)} != {len(h2)}")
        return False
    else:
        logging.debug(f"Headers have same number of fields: {len(h1)} == {len(h2)}")
        return True
