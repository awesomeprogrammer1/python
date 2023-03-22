import pytest
from fibonacchi_sequence import fib


@pytest.mark.parametrize(
    "fib_number, result",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (7, 8),
        (10, 34),
    ],
)
def test_fib(fib_number: int, result: int):
    assert fib(fib_number) == result



