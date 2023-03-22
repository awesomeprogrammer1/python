import pytest
from sum_of_range import sum_of_range_loop, sum_of_range_recursive



@pytest.mark.parametrize(
    "low_range, high_range, result_int",
    [
        (2, 5, 14),
        (-1, 1, 0),
        (-4, -1, -10),
        (5,5, 5),
    ],
)
def test_sum_of_range(low_range: int, high_range: int, result_int: int):
    assert sum_of_range_loop(low_range, high_range) == result_int
    assert sum_of_range_recursive(low_range, high_range) == result_int
