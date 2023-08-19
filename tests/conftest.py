import pytest

from context import diff_csv
import diff_csv.core


# create word list fixture
@pytest.fixture(scope="module")
def csv_file():
    fname = "testdata/forest_1.csv"
    row_dict = diff_csv.core.read_file_raw(fname)

    return row_dict
