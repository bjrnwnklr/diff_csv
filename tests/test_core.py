from context import package_name
import package_name.core


class TestCore:
    def test_dummy_func(self, setup_dummy):
        """Test dummy function - replace with actual test.
        Uses a fixture from `conftest.py`.
        """
        a, b = setup_dummy
        assert package_name.core.dummy_func(a, b) == 2
