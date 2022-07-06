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

filtered_list = []
for i in a:
    if i < 10 or i > 30:
        filtered_list.append(i)
print('Filtered list:')        
print(filtered_list)

sum_filtered_list = sum(filtered_list)
print(f"sum_filtered_list={sum_filtered_list}")

# assignment 3

average_filtered_list = sum_filtered_list / len(filtered_list)
print(f"average_filtered_list={average_filtered_list}")
