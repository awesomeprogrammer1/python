"""
Tests for set_gen.py

Tests:
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))
----------------------------------------------------------------------------
Result:
{1, 3, '111', '33', '11'}
{'5555555', 5, '55', '55555', '5555', '555555', '555'}
{1, 2, 3, 5, 6, 7, '22', '2222', '22222', '222', '11', '222222'}

"""

import pytest
from set_gen import set_gen


@pytest.mark.parametrize(
    "source_list, result_set",
    [
        ([1, 1, 3, 3, 1], {1, 3, "111", "33", "11"}),
        ([5, 5, 5, 5, 5, 5, 5], {"5555555", 5, "55", "55555", "5555", "555555", "555"}),
        (
            [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2],
            {1, 2, 3, 5, 6, 7, "22", "2222", "22222", "222", "11", "222222"},
        ),
    ],
)
def test_set_gen(source_list: list, result_set: set):
    assert result_set.symmetric_difference(set_gen(source_list)) == set()
