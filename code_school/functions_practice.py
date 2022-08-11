from random import randint


def secret(a: list) -> list:
    list_var = a.copy()
    list_var.pop(randint(0, len(a) - 1))
    return list_var


def secret_fix(a: list) -> tuple:
    # for element in a:
    #     if element not in list_variable:
    #         list_difference.append(element)
    #         return list_difference[0]
    local_var = secret(a)
    for element in a:
        if element not in local_var:
            return a, element


print(secret_fix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
