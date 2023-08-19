# diff_csv

A simple CSV file comparer.

- Compares headers of two CSV files - same columns, same column names, same order
- Compares rows of both files against each other by using a designated column as key

# Usage


# Files to customize before using

1. Change the package name and associated imports

-   Change imports:
    -   `package_name` directory:
        -   `core.py`
        -   `utils.py`
    -   `tests` directory:
        -   `context.py`
        -   `conftest.py`
        -   `test_core.py`
    -   `cli_app.py`: (Template for a CLI app, using the functions from the `core` and `utils` modules.)

1. Add required packages to the `req_initial.txt` file

# Other python templates

-   [rochacbruno's python project template](https://github.com/rochacbruno/python-project-template)
-   [PyScaffold](https://github.com/pyscaffold/pyscaffold)
-   [gvisoc's python project template](https://github.com/gvisoc/python-project-template)
