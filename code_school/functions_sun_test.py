import pytest
from functions_sun import sun
from functions_sun import sun2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("7:15", "Time = 7:15, Angle Of The Sun = 18.75"),
        ("2:00", "The Sun Is Down"),
        ("18:01", "The Sun Is Down"),
        ("6:00", "Time = 6:00, Angle Of The Sun = 0"),
        ("6:01", "Time = 6:01, Angle Of The Sun = 0.25"),
        ("17:59", "Time = 17:59, Angle Of The Sun = 179.75"),
        ("18:01", "Time = 18:00, Angle Of The Sun = 180"),
        ("12:00", "Time = 12:00, Angle Of The Sun = 90"),
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


@pytest.mark.parametrize(
    "hours,minutes,angle",
    [
        (7, 15, "Time = 7:15, Angle Of The Sun = 18.75"),
        (2, 0, "The Sun Is Down"),
        (18, 1, "The Sun Is Down"),
        (6, 0, "Time = 6:00, Angle Of The Sun = 0"),
        (6, 1, "Time = 6:01, Angle Of The Sun = 0.25"),
        (17, 59, "Time = 17:59, Angle Of The Sun = 179.75"),
        (18, 1, "Time = 18:00, Angle Of The Sun = 180"),
        (12, 0, "Time = 12:00, Angle Of The Sun = 90"),
        (-3, 0, "Error, Invalid Input"),
        (-3, -24, "Error, Invalid Input"),
        (3, -24, "Error, Invalid Input"),
        (13, -23, "Error, Invalid Input"),
        (-23, 24, "Error, Invalid Input"),
        (-23, 66, "Error, Invalid Input"),
        (66, 66, "Error, Invalid Input"),
        (15, 66, "Error, Invalid Input"),
        (66, 11, "Error, Invalid Input"),
    ],
)
def test_sun2(hours: int, minutes: int, angle: str):
    assert sun2(hours, minutes) == angle
