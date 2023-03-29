import pytest
from is_palindrome_int import is_palindrome_int

@pytest.mark.parametrize(
    "number, expected_result",
    [
        (101, True),
        (234, False),
        (1010101, True),
        (55, True),
        (524, False),
        (1241, False),
        (9, True),
    ],
)
def test_is_palindrome_int(number: int, expected_result: bool):
    assert is_palindrome_int(number) == expected_result
