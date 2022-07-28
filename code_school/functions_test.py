from functions import perimeter_area_rectangle_dict
from functions import print_perimeter_area_rectangle_dict


def test_perimeter_area_rectangle_dict():
    assert perimeter_area_rectangle_dict(6, 7) == {"A": 42, "P": 26}


def test_print_perimeter_area_rectangle():
    assert (
        print_perimeter_area_rectangle_dict(perimeter_area_rectangle_dict(6, 7))
        == "P = 26, A = 42"
    )
