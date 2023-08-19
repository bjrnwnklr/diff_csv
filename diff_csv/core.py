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
    h1 = f1[0]
    h2 = f2[0]

    # check number of columns is the same
    if len(h1) != len(h2):
        logging.error(f"Headers have different number of fields: {len(h1)} != {len(h2)}")
        return False
    else:
        logging.debug(f"Headers have same number of fields: {len(h1)} == {len(h2)}")

    # check that headers have the same names
    # We already know they have the same number of fields, so now test
    # - names of fields match
    # - at the same time, fields are in the same order
    mismatches = []
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            mismatches.append((i, h1[i], h2[i]))
    if mismatches:
        logging.error(f"Headers have mismatching fields: {mismatches}")
        return False
    else:
        logging.debug(f"Headers have matching fields.")

    return True
