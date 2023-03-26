import pytest
from list_practice import ranks, __sort_ranks


@pytest.mark.parametrize(
    "heights_list, height, expected_result",
    [
        ([162, 160, 154, 151], 150, 4),
        ([160, 164, 157, 158], 156, 4),
        ([162, 160, 154, 151], 155, 2),
        ([162, 160, 154, 151], 154, 3),
        ([162, 160, 154, 154], 154, 4),
    ],
)
def test_ranks(heights_list: list, height: int, expected_result: int):
    assert ranks(heights_list, height) == expected_result


@pytest.mark.parametrize(
    "source_list, expected_result",
    [
        ([162, 160, 154, 151], [162, 160, 154, 151]),
        ([160, 164, 157, 158], [164, 160, 158, 157]),
    ],
)
def test_sort_ranks(source_list: list, expected_result: list):
    assert __sort_ranks(source_list) == expected_result
