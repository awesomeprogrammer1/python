"""
Write a program that prints part of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5..
(a number is repeated as many times as it is equal to).
A non-negative integer n is passed to the input of the program —
this is how many elements of the sequence the program should display.
The output is expected to be a sequence of numbers separated by a space in one line.

For example, if n = 7, then the program should output 1 2 2 3 3 3 4 


"""


# def sequence_of_numbers(n: int) -> str:
#     num_str: str = ""
#     if n == 1:
#         return str(n)
#     for i in range(1, n):
#         if n*2-len(num_str) < i*2:
#             num_str += (str(i) + " ") * (n*2-len(num_str))
#             break
#         else:
#             num_str += (str(i) + " ") * i
#     return num_str[: n * 2 - 1]


def sequence_of_numbers(n: int) -> list:
    num_list: list = []
    if n == 1:
        return [n]
    


print(sequence_of_numbers(7))
