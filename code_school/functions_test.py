from functions import perimeter_area_rectangle_dict
from functions import print_perimeter_area_rectangle_dict


def test_perimeter_area_rectangle_dict():
    assert perimeter_area_rectangle_dict(6, 7) == {"Area": 42, "Perimeter": 26}


def test_print_perimeter_area_rectangle():
    assert (
        print_perimeter_area_rectangle_dict(perimeter_area_rectangle_dict(6, 7))
        == "Perimter = 26, Area = 42"
    )
