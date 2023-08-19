from context import diff_csv
import diff_csv.core


class TestCore:
    def test_file_to_dict(self):
        """Test the file_to_dict method"""
        fname = "testdata/forest_1.csv"
        row_dict = diff_csv.core.file_to_dict(fname)
        assert len(row_dict) == 271
