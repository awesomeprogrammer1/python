"""
Tests for order_str.py

Test cases:
print(all_eq(['крот', 'белка', 'выхухоль']))
print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
Results:
['крот____', 'белка___', 'выхухоль']
['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

"""

import pytest
from order_str import order_str


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
def test_order_str(source_list: list, result_list: list):
    assert  == set()
