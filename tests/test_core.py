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

    def test_changed_header_count(self, csv_file):
        """Test that changed header counts are being recognized correctly."""
        f1 = csv_file
        # load changed file
        fname = "testdata/forest_1_changed_headers_count.csv"
        f2 = diff_csv.core.read_file_raw(fname)
        assert diff_csv.core.headers_match(f1, f2) == False
