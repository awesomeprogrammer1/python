import pytest
from is_palindrome_int import is_palindrome_int

@pytest.mark.parametrize(
    "number, expected_result",
    [
        (2, 5, 14),
        (-1, 1, 0),
        (-4, -1, -10),
        (5,5, 5),
    ],
)
def test_is_palindrome_int(number: int, expected_result: bool):
    assert is_palindrome_int(number) == expected_result
