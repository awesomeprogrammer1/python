from random import randint


def secret(a: list) -> list:
    a.pop(randint(0, len(a) - 1))
    return a


list_variable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_difference = []


def secret_fix(a: list) -> int:
    for element in a:
        if element not in list_variable:
            list_difference.append(element)
            return list_difference[0]


print(secret(list_variable))


print(secret_fix(check_list))
