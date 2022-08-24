import pytest
from function_replace_in import function_in_papa, replace, replace2


@pytest.mark.parametrize(
    "source_str, char, expected_result",
    [
        ("hedgie", "h", True),
        ("hedgie", "d", True),
        ("hedgie", "s", False),
        ("hedgie", "H", False),
        ("Hedgie", "H", True),
        ("Hello", "llo", True),
        ("Hello", "He", True),
        ("Hello", "el", True),
        ("Andrew", "An", True),
    ],
)
def test_function_in_papa(source_str: str, char: str, expected_result: bool):
    assert function_in_papa(source_str, char) == expected_result


@pytest.mark.parametrize(
    "source_str, old_char, new_char, expected_result",
    [
        ("Hello", "H", "Y", "Yello"),
        ("Hello", "He", "Yo", "Yollo"),
        ("Hello", "ll", "mm", "Hemmo"),
        ("Hedgie", "t", "m", "Hedgie"),
        ("Hedgie", "tr", "m", "Hedgie"),
        ("Hello Hello", "ll", "mm", "Hemmo Hemmo"),
        ("Hi Alladin", "Alladin", "Andrew", "Hi Andrew"),
    ],
)
def test_replace(source_str: str, old_char: str, new_char: str, expected_result: str):
    assert replace(source_str, old_char, new_char) == expected_result
    assert replace2(source_str, old_char, new_char) == expected_result
