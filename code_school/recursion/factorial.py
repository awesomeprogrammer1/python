# 5! = 1*2*3*4*5


# def factorial(num: int) -> int:
#     factorial_var = 1
#     for i in range(1, num + 1):
#         factorial_var *= i
#     return factorial_var


# def sum(num1: int, num2: int) -> int:
#     sum_var = 0
#     for i in range(num1, num2 + 1):
#         sum_var += i
#         print(i)
#     return sum_var
# a = 3
# print(a)
# print(factorial(a))
# print(a)
# print(sum(1, 5))



def get_number(num: int) -> int:
    if num == 0:
        return 1
    else:
        return get_number(num-1)

# get_number(num-1) = get_number(num-1-1) = get_number(num-1-1-1) = get_number(num-1-1-1-1) = 1

print(get_number(5))


def factorial(num: int):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
# factorial(5) = 5 * factorial( 5-1) = 4 * factorial( 5-1-1)= 3 * factorial(5-1-1-1) = 2 * factorial(5-1-1-1-1) = 1 * factorial (5-1-1-1-1-1) = 1
# factorial(5) = 5 * 24 = 4 * 6= 3 * 2 = 2 * 1 = 1 * 1 = 1
print(factorial(5))
