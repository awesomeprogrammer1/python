import pytest
from largest_elem_in_list import largest_element_index, __largest_element


@pytest.mark.parametrize(
    "list_of_str, result",
    [
        (["apple", "mango", "avocado"], 2),
        (["fruit", "vegetables", "yogurt", "vegetables"], 1),
        (["apple", "ball"], 0),
    ],
)
def test_largest_element_index(list_of_str: list, result: int):
    assert largest_element_index(list_of_str) == result


@pytest.mark.parametrize(
    "list_of_str, result",
    [
        (["apple", "mango", "avocado"], "avocado"),
        (["fruit", "vegetables", "yogurt", "vegetables"], "vegetables"),
        (["apple", "ball"], "apple"),
    ],
)
def test_largest_element(list_of_str: list, result: str):
    assert __largest_element(list_of_str) == result
