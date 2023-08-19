import pytest

# uncomment if any functions are required from the package
# to set up any fixtures, e.g. DB connections
# from context import package_name


# create word list fixture
@pytest.fixture(scope="module")
def csv_file():
    fname = "testdata/forest_1.csv"
    row_dict = diff_csv.core.file_to_dict(fname)

    return row_dict
