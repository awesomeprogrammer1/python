import pytest
from is_palindrome import is_palindrome, __reverse_str



@pytest.mark.parametrize(
    "source_str, expected_result",
    [
        ("cat", False),
        ("Racecar", False),
        ("hannah", True),
        ("Apple", False),
    ],
)
def test_is_palindrome(source_str: str, expected_result: bool):
    assert is_palindrome(source_str) == expected_result


@pytest.mark.parametrize(
    "source_str, expected_result",
    [
        ("cat", "tac"),
        ("Racecar", "racecaR"),
        ("hannah", "hannah"),
        ("Apple", "elppA"),
    ],
)
def test_reverse_str(source_str: str, expected_result: str):
    assert __reverse_str(source_str) == expected_result





