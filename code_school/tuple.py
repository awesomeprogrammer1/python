# list_variable = [1,2,3,4]
# list_variable[0] = 4
# print(list_variable)
# tuple_variable = 1,0,


s = "fdfw"
# print(tuple_variable)

# the difference between these two for statements is that the first
# for loop prints out the same string a certain amount of times
# (to be specific, it prints out the string the amount of times equal to the amount of characters in the string)
# the second loop prints out each individual letter
for i in range(len(s)):
    print(s)
for e in s:
    print(e)


# def f1(s: str) -> tuple:
#     list_variable = []
#     s = input("Write a string of letters")
#     for i in range(len(s)):
#         list_variable.append(i)
#     return list_variable
