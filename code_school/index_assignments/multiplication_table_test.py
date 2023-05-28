import pytest
from multiplication_table import multiplication_table


@pytest.mark.parametrize(
    "low_range1, high_range1, low_range2, high_range2, result",
    [
        (7, 10, 5, 6, [5, 6, 7, 35, 42, 8, 40, 48, 9, 45, 54, 10, 50, 60]),
        (3, 6, 2, 4, [2, 4, 3, 6, 12, 4, 8, 16, 5, 10, 20, 6, 12, 24]),
    ],
)
def test_multiplication_table(low_range1: int, high_range1: int, low_range2: int, high_range2: int, result: list):
    assert (multiplication_table(low_range1, high_range1, low_range2, high_range2)) == result
