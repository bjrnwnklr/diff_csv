import logging
import argparse
from pathlib import Path
import diff_csv.core
import diff_csv.utils


@diff_csv.utils.runtimer
def the_main_function(fname1: str, fname2: str, id_col: str) -> None:
    """Compare two CSV files with each other."""

    # read in the first file
    f1 = file_to_dict(fname1)
    logging.info(f"Read file {fname1} with {len(f1)} rows")

    # read second file
    f2 = file_to_dict(fname2)
    logging.info(f"Read file {fname2} with {len(f2)} rows")

    # start comparing
    # 1) check headers are the same - same number, same order, same names

    # 2) check rows per file and report difference

    # 3) create hashes per row in two separate dictionaries and compare them
    #    Report on
    #    - key from 2nd file not found in 1st file
    #    - mismatch of hash between two keys


def main():
    """Main function, sets up argument parsing."""

    parser = argparse.ArgumentParser(epilog="Compare two CSV files for structure and matching rows.")
    parser.add_argument("file1", type=str, help="First CSV path/filename to load")
    parser.add_argument("file2", type=str, help="Second CSV path/filename to load")
    parser.add_argument("id", type=str, help="Column name to use as key to match rows")
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

    the_main_function(fname1, fname2, id_col)


if __name__ == "__main__":
    main()
