from easygui import *

list = [1, 2, 3, 4, 5]

list.append(6)  # operation: adds 6 to the end of the list
print(list)

list.insert(3, "Alex")  # operation: inserts "Alex" at the index 3
print(list)

list.remove(3)  # operation: Removes the integer "3" from the list
print(list)

list = [1, 2, 3, 4, 5]
# removes the middle number, since we count from 5 if its a negative number, it removes the integer  "4"
list.pop(-2)
print(list)

# operation: inputs "Andrew" instead of the 2nd index, so it would change 5 for "Andrew"
list[3] = "Andrew"
print(list)

# operation: presented with a list. the for statement runs until there are 100 zeros in the list.
list = [1, 1]
for i in range(100):
    list.insert(1, 0)
print(list)

# this piece of code prints every even number from 2 to one hundred
list = []
for i in range(2, 101, 2):
    list.append(i)
print(list)


# list asks for a name, if the input matches something in the list, it executes a piece of code. If it doesn't it runs different piece of code
list = ["Alex", "Sergey", "Andrew"]
name = enterbox("Hello! What is your name? ")
if name in list:
    msgbox("Welcome")
else:
    msgbox("sorry, not today")

# operation: presented with a list: we are multiplying every even number by two
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 10, 2):
    list[i] = list[i] * 2
print(list)

# checking if a condition holds true. If it is true, that data is sorted to the new list.
for i in list:
    if i < 3 or i > 7:
        print(i)
print(list)
