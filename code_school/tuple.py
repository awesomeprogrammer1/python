


list_variable = [1, 2, 3, 4]
list_variable[0] = 4
print(list_variable)
tuple_variable = (
    1,
    0,
)
print(tuple_variable)


s = "fdfw"
# print(tuple_variable)


# Iterable - Iterable is an object which can be looped over or iterated over
# with the help of a for loop. 
# Objects like
# lists, tuples, sets, dictionaries, strings, etc.are called iterables.
# In short and simpler terms, iterable is anything that you can loop over.


# the difference between these two for statements is that the first
# for loop prints out the same string a certain amount of times
# (to be specific, it prints out the string the amount of times equal to the amount of characters in the string)
# the second loop prints out each individual letter
# additionally, i is an integer, while "e" is a string
for i in range(len(s)):
    print(i)
for e in s:
    print(e)


# def f1(s: str) -> tuple:
#     list_variable = []
#     s = input("Write a string of letters")
#     for i in range(len(s)):
#         list_variable.append(i)
#     return list_variable
