import pytest
from sequence_of_int_backup import sequence_of_int

@pytest.mark.parametrize(
    "list_of_int, result",
    [
        ([1,3,4,2,0], [0,2,4,3,1]),
        ([4,8,9,0],[0,9,8,4]),
        ([4,5,23,7,49, 11, 87, 0], [0, 87, 11, 49, 7, 23, 5, 4]), 
    ],
)
def test_sequence_of_int(list_of_int: list, result: list):
    assert sequence_of_int(list_of_int) == result
