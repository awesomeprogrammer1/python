from functions import perimeter_area_rectangle_dict
from functions import print_perimeter_area_rectangle_dict
from functions import get_perimeter_area_tuple


def test_perimeter_area_rectangle_dict():
    assert perimeter_area_rectangle_dict(6, 7) == {"Area": 42, "Perimeter": 26}


def test_print_perimeter_area_rectangle():
    assert (
        print_perimeter_area_rectangle_dict(perimeter_area_rectangle_dict(6, 7))
        == "Perimeter = 26, Area = 42"
    )


def test_get_perimeter_area_tuple():
    assert get_perimeter_area_tuple(10, 1) == ("Perimeter = 22", "Area = 10")
