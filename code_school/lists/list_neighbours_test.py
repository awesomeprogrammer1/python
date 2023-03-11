import pytest
from list_neighbours import list_neighbours

@pytest.mark.parametrize(
    "source_list, expected_result",
    [
        ([1,2,3], 0),
        ([1,3,2], 1),
        ([], 0),
        ([1], 0),
        ([1,2], 0),
        ([1,3,2,4,7,5, 8, 13, 2], 3),
    ],
)
def test_list_neighbours(source_list: list, expected_result: int):
    assert list_neighbours(source_list) == expected_result