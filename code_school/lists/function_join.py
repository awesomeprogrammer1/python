from operator import index


hey: list = ["hi", "andrew"]
hey2: list = ["hi", "papa"]
counter = 0


def join_func(list1: list, separator: str) -> str:
    joined_str = ""
    counter = 0
    # creating new str
    for element in list1:
        joined_str += element
        # adds the element to the string
        if counter == 0:
            joined_str += separator
            # adds seperator to string
            counter += 1
        else:
            pass
        # adds the seperator after the element to the string
    return joined_str


print(join_func(hey, "..."))
# testing case 1
print(join_func(hey2, "..."))
# testing case 2


# def sum(number1, number2):
#     return number1 + number2


# print(sum(number1=5, number2=10))
# print(sum(number1=15, number2=7))
# a = 7
# b = 8
# print(sum(number1=a, number2=b))
