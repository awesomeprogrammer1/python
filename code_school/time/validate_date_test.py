import pytest
from validate_date import is_valid_date


@pytest.mark.parametrize(
    "date_str, date_format_type, expected_result",
    [
        ("2022-09-01", "%Y-%m-%d", True),
        ("2022-44-55", "%Y-%m-%d", False),
        ("2021-02-11", "%Y-%d-%m", True),
        ("hedgie", "%m/%d/%y", False),
        ("2022-21-13", "%Y-%m-%d", False),
        ("2021-02-12", "%Y-%d-%m", True),
        ("2021-02-29", "%Y-%d-%m", False),
        ("1982-23-11", "", False),
        ("03/31/2022", "%m/%d/%y", False),
        ("02/29/2020", "%m/%d/%Y", True),
        ("20/12/2020", "%d/%m/%Y", True)
    ],
)
def test_is_valid_date(date_str: str, date_format_type: str, expected_result: bool):
    assert is_valid_date(date_str, date_format_type) == expected_result
