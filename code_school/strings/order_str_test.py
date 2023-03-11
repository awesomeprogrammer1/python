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
    "source_list, result_list",
    [
        (['крот', 'белка', 'выхухоль'], ['крот____', 'белка___', 'выхухоль']),
        (['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']),
        (
            ['qweasdqweas', 'q', 'rteww', 'ewqqqqq'],
            ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____'],
        ),
    ],
)
def test_order_str(source_list: list, result_list: list):
    assert order_str(source_list) == result_list
