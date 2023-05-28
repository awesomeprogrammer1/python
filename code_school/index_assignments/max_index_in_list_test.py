import pytest
from max_index_in_list import max_index, __max_element


@pytest.mark.parametrize(
    "list_of_int, result",
    [
        ([4, 8, 9, 0, 7, 11, 4, 3, 11, 2], 5),
        ([34, 72, 94, 26, 19, 8, 42, 87, 107], 8),
    ],
)
def test_max_index(list_of_int: list, result: int):
    assert max_index(list_of_int) == result


@pytest.mark.parametrize(
    "list_of_int, result",
    [
        ([1, 3, 4, 2, 0], 4),
        ([4, 8, 9, 0, 7, 11, 4, 3, 11, 2], 11),
        ([34, 72, 94, 26, 19, 8, 42, 87, 107], 107),
    ],
)
def test_max_element(list_of_int: list, result: int):
    assert __max_element(list_of_int) == result
