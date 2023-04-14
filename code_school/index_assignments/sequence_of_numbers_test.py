import pytest
from sequence_of_numbers import sequence_of_numbers


@pytest.mark.parametrize(
    "n, result",
    [
        (7, '1 2 2 3 3 3 4'),
        (1, '1'),
        (8, '1 2 2 3 3 3 4 4'),
    ],
)
def test_sequence_of_numbers(n: int, result: str):
    assert sequence_of_numbers(n) == result
