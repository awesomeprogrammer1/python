a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
from typing import List
from easygui import *

# assignment 1: print all numbers that are less than 5
# assignment 2: print the sum of the elements less than 10 and bigger than 30
# assignment 3: learn about averages and print the average of elements in the list

# assignment 1

for i in a:
    if i < 5:
        print(i)

# assignment 2

filteredList = []
List = []
for i in a:
    if i < 10 or i > 30:
        filteredList.append(i)
print(filteredList)
for i in a:
    if i < 10:
        filteredList.remove(i)
        List.append(i)
print(List)
print(filteredList)





sum1 = sum(List)
print(sum1)

sum2 = sum(filteredList)
print(sum2)



# assignment 3

sum = 0
for i in a:
    sum += i
average = sum / len(a)
print(sum, average)
