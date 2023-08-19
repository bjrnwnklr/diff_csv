from context import diff_csv
import diff_csv.core


class TestCore:
    def test_read_file_raw(self):
        """Test the read_file_raw method by reading in a sample file.
        Expected length including one header row: 272.
        """
        fname = "testdata/forest_1.csv"
        row_dict = diff_csv.core.read_file_raw(fname)
        assert len(row_dict) == 272
