'''
Write a function fib(n) that, given a non-negative integer n, 
returns the nth Fibonacci number. 
You can't use loops in this problem - use recursion.


'''


# def fib(fib_number: int) -> int:
#     number_1 = 0
#     number_2 = 1
#     if fib_number == 1:
#         return 0
#     else:
#         for i in range(fib_number-2):
#             number_1, number_2 = number_2, number_1+number_2
#         return number_2


def fib(fib_number: int) -> int:
    if fib_number == 1:
        return 0
    elif fib_number == 2:
        return 1
    else:
        return fib(fib_number-1)+fib(fib_number-2)
