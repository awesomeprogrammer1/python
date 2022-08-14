import pytest
from function_replace_in import function_in
from function_replace_in import replace


@pytest.mark.parametrize(
    "source_str, char, expected_result",
    [
        ("hedgie", "h", True),
        ("hedgie", "d", True),
        ("hedgie", "s", False),
        ("hedgie", "H", False),
        ("Hedgie", "H", True),
    ],
)
def test_function_in(source_str: str, char: str, expected_result: bool):
    assert function_in(source_str, char) == expected_result


@pytest.mark.parametrize(
    "source_str, old_char, new_char, expected_result",
    [
        ("Hello", "H", "Y", "Yello"),
    ],
)
def test_replace(source_str: str, old_char: str, new_char: str, expected_result: str):
    assert replace(source_str, old_char, new_char) == expected_result
