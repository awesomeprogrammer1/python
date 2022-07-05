from easygui import *

list = [1, 2, 3, 4, 5]

list.append(6)  # operation: adds 6 to the list
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

# operation: inserts the integer "0" 100 times by running a for statement which runs 100 times
list = [1, 1]
for i in range(100):
    list.insert(1, 0)
print(list)

# prints all the even numbers in the list by skip counting by two
list = []
for i in range(2, 101, 2):
    list.append(i)
print(list)


# list that checks an input and executes a piece of code depending on the data
list = ["Alex", "Sergey", "Andrew"]
name = enterbox("Hello! What is your name? ")
if name in list:
    msgbox("Welcome")
else:
    msgbox("sorry, not today")

# operation: multiplies every second number in the list by two repeatedly using a for statement
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 10, 2):
    list[i] = list[i] * 2
print(list)

# checks the condition that if i is less than three of greater than 7. If the condition holds true, it prints the integer
for i in list:
    if i < 3 or i > 7:
        print(i)
print(list)
