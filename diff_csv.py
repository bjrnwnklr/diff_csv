import sys
import logging
import argparse
from pathlib import Path
import diff_csv.core
import diff_csv.utils


@diff_csv.utils.runtimer
def the_main_function(fname1: str, fname2: str, id_col: str) -> None:
    """Compare two CSV files with each other."""

    # read in the first file
    # f1 = diff_csv.core.file_to_dict(fname1)
    f1 = diff_csv.core.read_file_raw(fname1)
    logging.debug(f"Read file {fname1} with {len(f1)} rows")

    # read second file
    f2 = diff_csv.core.read_file_raw(fname2)
    logging.debug(f"Read file {fname2} with {len(f2)} rows")

    # start comparing
    # 1) check headers are the same - same number, same order, same names
    # check number of columns is the same
    if not diff_csv.core.headers_match(f1, f2):
        print("Headers do not match, see error messages for details")
        sys.exit()

    # 2) check rows per file and report difference
    if not diff_csv.core.row_count_match(f1, f2):
        print("Row counts are different, see error messages for details")
        # do not exit here, we still want to compare the lines since headers match.

    # 3) create hashes per row in two separate dictionaries and compare them
    #    Report on
    #    - key from 2nd file not found in 1st file
    #    - mismatch of hash between two keys
    mismatches = diff_csv.core.row_match(f1, f2, id_col)


def main():
    """Main function, sets up argument parsing."""

    parser = argparse.ArgumentParser(epilog="Compare two CSV files for structure and matching rows.")
    parser.add_argument("file1", type=str, help="First CSV path/filename to load")
    parser.add_argument("file2", type=str, help="Second CSV path/filename to load")
    parser.add_argument("id_col", type=str, help="Column name to use as key to match rows")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    # check if --verbose was set
    if args.verbose:
        # set logging level to INFO
        logging.basicConfig(level=logging.INFO)
    else:
        # standard is ERRORS only
        logging.basicConfig(level=logging.ERROR)

    # check if first file exists, if not exit
    fname1 = args.file1
    p = Path(fname1)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {fname1}")

    # check if second file exists, if not exit
    fname2 = args.file2
    p = Path(fname2)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {fname2}")

    the_main_function(fname1, fname2, args.id_col)


if __name__ == "__main__":
    main()
