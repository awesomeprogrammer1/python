"""
Write a program that reads numbers from the console (one per line)
until the sum of the entered numbers is 0 and immediately after that
prints the sum of the squares of all the numbers read.

It is guaranteed that at some point
the sum of the entered numbers will be equal to 0,
after which there is no need to continue reading.

In the example, we read the numbers 1, -3, 5, -6, -10, 13; at this point,
we notice that the sum of these numbers is equal to zero
and print the sum of their squares,
ignoring the fact that there are still unread values.

Example:
Input:
1, -3, 5, -6, -10, 13
Output:
340

"""


def sum_of_squares(list_of_num: list) -> int:
    sum_squares = 0
    for num in list_of_num:
        sum_squares += num ** 2
    return sum_squares


def read_numbers() -> list:
    list_of_num = []
    sum_of_num = 1
    while sum_of_num != 0:
        current_num_input = int(input("Enter positive or negative numbers to square. Once the sum of all the numbers you have entered reaches zero, the program will stop. "))
        list_of_num.append(current_num_input)
        sum_of_num = sum(list_of_num)
    return list_of_num
        


def main():
    sum = sum_of_squares(read_numbers())
    print(sum)


if __name__ == "__main__":
    main()