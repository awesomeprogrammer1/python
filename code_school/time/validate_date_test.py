import pytest
from validate_date import is_valid_date


@pytest.mark.parametrize(
    "date_str, expected_result",
    [
        ("2022-09-01", True),
        ("2022-44-55", False),
        ("hedgie", False),
        ("2022-21-12", False),
        ("2021-02-29", False),
    ],
)
def test_is_valid_date(date_str: str, expected_result: bool):
    assert is_valid_date(date_str) == expected_result
