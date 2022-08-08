from random import randint




def secret(a : list) -> list:

    a.pop(randint(0, len(a) - 1))
    return a
list_variable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(secret(list_variable))

def secret_fix():



