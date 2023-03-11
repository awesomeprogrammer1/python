# 5! = 1*2*3*4*5


def factorial(num: int) -> int:
    factorial_var = 1
    for i in range(1, num + 1):
        factorial_var *= i
    return factorial_var


# def sum(num1: int, num2: int) -> int:
#     sum_var = 0
#     for i in range(num1, num2 + 1):
#         sum_var += i
#         print(i)
#     return sum_var
a = 3
print(a)
print(factorial(a))
print(a)
# print(sum(1, 5))
