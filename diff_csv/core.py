import diff_csv.utils
import csv
import logging
import hashlib


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


def row_count_match(f1, f2) -> bool:
    """Return if row count of both files match."""
    if len(f1) != len(f2):
        logging.error(f"Row count different between both files: {len(f1)} != {len(f2)}")
        return False
    else:
        return True


def hash_dict(f, id_col) -> dict:
    """Return a dictionary of id_col : hashvalues of the given list of rows.
    First row is assumed to be the header row that contains the id_col name.
    """
    header, rows = f[0], f[1:]

    # check if id_col is in header
    if id_col not in header:
        logging.error(f"ID column name {id_col} not found in header of file: {header}")
        sys.exit

    # find index of id_col in header
    id_idx = header.index(id_col)

    # create dict of hashvalues
    return {row[id_idx]: hashlib.sha256(",".join(row).encode()).hexdigest() for row in rows}


def row_match(f1, f2, id_col) -> list:
    """Return rows that mismatch.
    Match by the given id column, which has be exist in both files.

    Calculates a sha256 hash value per row and compares entries with the same
    value in the id column.

    Returns a list of mismatches by comparing all ids from f2 with ids in f1.
    Will return a mismatch if:
    - f2 has an id that is not in f1
    - hashes do not match for the same id in f1 and f2

    Will not return mismatches if:
    - f1 has more rows than f2, i.e. not all f1 ids get checked.
    """
    # create a dictionary for of id_col : sha256 hashvalue for both files
    f1_dict = hash_dict(f1, id_col)
    f2_dict = hash_dict(f2, id_col)

    # compare keys from f2 to f1 and match hashes

    not_found_f1 = []
    not_found_f2 = []
    mismatches = []

    logging.info(f"Comparing keys from file2 with file1.")
    for k in f2_dict:
        if k not in f1_dict:
            logging.error(f"Key {k} not found in file.")
            not_found_f1.append(k)
        elif f1_dict[k] != f2_dict[k]:
            logging.error(f"Row values mismatch for key {k}.")
            mismatches.append(k)

    logging.info(f"Comparing keys from file1 with file2.")
    for k in f1_dict:
        if k not in f2_dict:
            logging.error(f"Key {k} not found in file.")
            not_found_f2.append(k)

    return not_found_f1, not_found_f2, mismatches
