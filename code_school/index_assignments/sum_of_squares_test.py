import pytest
from sum_of_squares import sum_of_squares


@pytest.mark.parametrize(
    "lst_of_num, result",
    [
        ([1, -1], 2),
        ([1, -3, 5, -6, -10, 13], 340),
    ],
)
def test_sum_of_squares(lst_of_num: list, result: int):
    assert sum_of_squares(lst_of_num) == result




