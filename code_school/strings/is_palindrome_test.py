import pytest
from is_palindrome import is_palindrome


@pytest.mark.parametrize(
    "source_str, expected_result",
    [
        ("cat", False),
        ("Racecar", True),
        ("hannah", True),
        ("Apple", False),
    ],
)
def test_is_palindrome(source_str: str, expected_result: bool):
    assert is_palindrome(source_str) == expected_result




