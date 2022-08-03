import pytest
from functions_sun import sun


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("7:15", "Time = 7:15, Angle Of The Sun = 18.75"),
        ("2:00", "Time = 2:00, The Sun Is Down"),
        ("12:00", "Time = 12:00, Angle Of The Sun = 90.0"),
        ("17:59", "Time = 17:59, Angle Of The Sun = 179.75"),
        ("18:00", "Time = 18:00, Angle Of The Sun = 180.0"),
        ("18:01", "Time = 18:01, The Sun Is Down"),
        ("5:59", "Time = 5:59, The Sun Is Down"),
        ("6:00", "Time = 6:00, Angle Of The Sun = 0.0"),
        ("6:01", "Time = 6:01, Angle Of The Sun = 0.25"),
        ("-3:00", "Error, Invalid Input"),
        ("-3:-24", "Error, Invalid Input"),
        ("13:-24", "Error, Invalid Input"),
        ("3:-24", "Error, Invalid Input"),
        ("abc", "Error, Invalid Input"),
        ("ab:cd", "Error, Invalid Input"),
    ],
)
def test_sun(test_input: str, expected: str):
    assert sun(test_input) == expected
