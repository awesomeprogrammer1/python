import pytest
from define_dict import top3


@pytest.mark.parametrize(
    "source_str, expected_result",
    [
        ("col caun lreo", "Symbol/Frequency: c/2, o/2, l/2"),
    ],
)
def test_top3(source_str: str, expected_result: str):
    assert top3(source_str) == expected_result


def test_top3_long_sentence():
    test_sentence="""
    discovered america think that one or more of their ships 
    were blown off course and 
    ended up in the northeast united states
"""
    assert top3(test_sentence) == "Symbol/Frequency: e/15, t/10, o/9"