import pytest

# uncomment if any functions are required from the package
# to set up any fixtures, e.g. DB connections
# from context import package_name


@pytest.fixture(scope="module")
def setup_dummy():
    a = 1
    b = 1
    return (a, b)


# Example fixtures:
# # create word list fixture
# @pytest.fixture(scope="module")
# def setup_words():
#     fname = "testdata/english-answers-alphabetical.txt"
#     words = wordle.utils.load_word_list(fname)

#     return words


# # create pattern_matrix
# @pytest.fixture(scope="module")
# def setup_pattern_matrix(setup_words):
#     words = setup_words
#     pm = wordle.core.generate_pattern_matrix(words)

#     return pm
