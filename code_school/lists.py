from easygui import *

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# assignment 1: print all numbers that are less than 5
# assignment 2: print the sum of the elements less than 10 and bigger than 30
# assignment 3: learn about averages and print all averages in the ray


# list = [1,2,3,4,5]

# list.append(6) # operation: adds 6 to the list
# print(list)

# list.insert(3, "Alex") # operation: changes the integer '3' with "Alex"
# print(list)

# list.remove(3) # operation: Removes the integer "3" from the list
# print(list)

# list.pop(-2) # removes the middle number, since we count from 5 if its a negative number, it removes the integer  "3"
# print(list)

# list[3]= "Andrew" # operation: inputs "Andrew" instead of the 2nd index, so it would change 3 for "Andrew"
# print(list)

# list = [1, 1]
# for i in range(100):
#     list.insert(1, 0)
# print(list)

# list = []
# for i in range(2, 101, 2):
#     list.append(i)
# print(list)

# list = ["Alex", "Sergey", "Andrew"]
# name = enterbox('Hello! What is your name? ')
# if name in list:
#     msgbox('Welcome')
# else:
#     msgbox('sorry, not today')

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(1, 10, 2):
#     list[i] = list[i] * 2
# print(list)

# for i in list:
#     if i < 3 or i > 7:
#         print(i)

# assignment 1

# for i in a:
#     if i < 5:
#         print(i)

# assignment 2


# for i in a:
#     if i < 10 or i > 30:
#         print(i)
# newList = a[:6] + a[8:]
# print(newList)
# newList[6:7]
# newerList = newList[6:9]
# print(newerList)
# newestList = newList[1:6]
# print(newestList)
# sum1 = 0
# for i in newerList:
#     sum1 += i
# average = sum1 / len(newerList)
# print(sum1, average)

# sum2 = 0
# for i in newestList:
#     sum2 += i
# average = sum2 / len(newestList)
# print(sum2, average)


# assignment 3

# sum = 0
# for i in a:
#     sum += i
# average = sum / len(a)
# print(sum, average) 
