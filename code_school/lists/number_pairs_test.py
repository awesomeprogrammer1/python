import pytest
from number_pairs import number_pairs


@pytest.mark.parametrize(
    "source_list, expected_result",
    [
        ([1,2,3], [1,2]),
        ([1,-2, 3, 4], [3,4]),
        ([], []),
        ([1], []),
        ([1,2], [1,2]),
        ([1,-3,2,-4,7,5, -8, -13, 2], [7,5]),
        ([-3,-5, 7, -4, 2, 3, -8], [-3, -5]),
    ],
)
def test_number_pairs(source_list: list, expected_result: list):
    assert number_pairs(source_list) == expected_result