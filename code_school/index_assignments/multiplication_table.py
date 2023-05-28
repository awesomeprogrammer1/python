"""

When Pavel was at school, 
he memorized the multiplication table in rectangular blocks. 
For training, a program that would show 
a block of the multiplication table would be very useful to him.

Create a function that creates a multiplication table
With 4 input values, 2 each being the range of the table


Example:
multiplication_table(7,10,5,6)
[5, 6, 7, 35, 42, 8, 40, 48, 9, 45, 54, 10, 50, 60]

"""


def multiplication_table(low_range1: int, high_range1: int, low_range2: int, high_range2: int) -> list:
    mult_lst: list = [low_range2, high_range2]
    for i in range(low_range1, high_range1 + 1):
        current_nums = [i, i * low_range2, i * high_range2]
        mult_lst += current_nums
    return mult_lst


print(multiplication_table(7, 10, 5, 6))
