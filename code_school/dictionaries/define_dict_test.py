import pytest_lazyfixture


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