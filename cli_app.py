import logging
import argparse
from pathlib import Path
import package_name.core
import package_name.utils


@package_name.utils.runtimer
def the_main_function(fname: str) -> None:
    """The real main function - add functionality here, using the package's core
    and utils modules."""

    # do something here
    print(package_name.core.dummy_func(1, 1))


def main():
    """Main function, sets up argument parsing."""

    parser = argparse.ArgumentParser(epilog="Add description of program's function.")
    parser.add_argument("file", type=str, help="path/filename to load")
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    args = parser.parse_args()

    # check if --verbose was set
    if args.verbose:
        # set logging level to INFO
        logging.basicConfig(level=logging.INFO)
    else:
        # standard is ERRORS only
        logging.basicConfig(level=logging.ERROR)

    # check if file exists, if not exit
    fname = args.file
    p = Path(fname)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {fname}")

    the_main_function(fname)


if __name__ == "__main__":

    main()
