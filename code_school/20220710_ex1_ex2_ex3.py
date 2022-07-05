a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
from easygui import *

# assignment 1

# for i in a:
#     if i < 5:
#         print(i)

# assignment 2

newList = []
newerList = []
for i in a:
    if i < 10 or i > 30:
        newList.append(i)
print(newList)
for i in a:
    if i < 10:
        newList.remove(i)
        newerList.append(i)
print(newerList)
print(newList)


# b = a[:6] + a[8:]
# print(b)
# b[6:7]
# c = b[6:9]
# print(c)
# d = b[1:6]
# print(d)


sum1 = sum(newerList)
print(sum1)

sum2 = sum(newList)
print(sum2)


# sum1 = 0
# for i in b:
#     sum1 += i

# print(sum1)


# sum1 += i
# average = sum1 / len(c)
# print(sum1, average)

# sum2 = 0

# sum2 += i
# average = sum2 / len(d)
# print(sum2, average)


# assignment 3

# sum = 0
# for i in a:
#     sum += i
# average = sum / len(a)
# print(sum, average)
