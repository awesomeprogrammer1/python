from typing import Tuple

# assignment 1:
# write the perimeter_area_rectangle function in one line
# assignment 2:
# write a program called "calculator" with the help of functions
# with plus, minus, multiply, and divide
# assignment 3:
# {"P":123,"A":123}
# create a version of perimeter_area_rectangle where
# the returned value is a dictionary and not a formatted string
# additionally, create a function called "print_perimeter_area_rectangle"
# and the function prints out the original formatted string
# assignment 4:
# learn about assert

# def math(a, b):
#     return a+b


# print(math(b=5, a=2)) #print(7)
# c = math(7,9)
# print(c)

# a = 'hello'
# b = len(a)
# print(b)

# def strlength(a):
#     return len(a)


# print(strlength(input('Write Anything: ')))

# P= 123, Area=123
# dict = {}


# def print_perimeter_area_rectangle(width, height):
#     return f"Perimeter = {(width+height)*2}, Area = {width * height}"

# print(print_perimeter_area_rectangle(5, 4))


def perimeter_area_rectangle_dict(width, height):
    dict = {}
    dict["Area"] = width * height
    dict["Perimeter"] = (width + height) * 2
    return dict


def print_perimeter_area_rectangle_dict(dict: dict):
    area = dict["Area"]
    perimeter = dict["Perimeter"]
    return f"Perimeter = {perimeter}, Area = {area}"


# print(perimeter_area_rectangle_dict(6, 7))
dict = {"Area": 56, "Perimeter": 30}
print(print_perimeter_area_rectangle_dict(dict))

# assignment 2
# "Perimeter = 40", "Area = 100"


def width_height_area_dict(width, height):
    area = width * height
    perimeter = (width + height) * 2
    return f"Perimeter = {perimeter}, Area = {area}"


# print(width_height_area_dict(10, 10))


def get_perimeter_area_tuple(height: int, width: int) -> Tuple[str, str]:
    return f"Perimeter = {(height+width)*2}", f"Area = {height*width}",


print(str(get_perimeter_area_tuple(1, 10)))
