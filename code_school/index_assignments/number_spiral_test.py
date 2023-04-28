import pytest
from number_spiral import number_sprial


@pytest.mark.parametrize(
    "n, result",
    [
        (5, [1, 2, 3, 4, 5, 16, 17, 18, 19, 6, 15, 24, 25, 20, 7, 14, 23, 22, 21, 8, 13, 12, 11, 10, 9]),
    ],
)
def test_number_sprial(n: int, result: list):
    assert number_sprial(n) == result

