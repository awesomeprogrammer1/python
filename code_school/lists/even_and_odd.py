list_of_integers = []
for i in range(-10, 0):
    list_of_integers.append(i)
for i in range(1, 11):
    list_of_integers.append(i)
print(list_of_integers)
# assignment 1
base_number = 0
for int in list_of_integers:
    if int < 0:
        base_number += int
print(base_number)
# assignment 2
base_number = 0
for int in list_of_integers:
    if int % 2 == 0:
        base_number += int
print(base_number)
# assignment 3
base_number = 0
for int in list_of_integers:
    if int % 2 != 0:
        base_number += int
print(base_number)
# assignment 4
base_number = 1
for i in range(len(list_of_integers)):
    if i % 3 == 0:
        base_number = base_number * list_of_integers[i]
print(base_number)
# assignment 5
smallest_number = min(list_of_integers)
smallest_number_index = list_of_integers.index(smallest_number)
biggest_number = max(list_of_integers)
biggest_number_index = list_of_integers.index(biggest_number)
print(list_of_integers[smallest_number_index:biggest_number_index])
range_of_numbers = list_of_integers[smallest_number_index:biggest_number_index]
product = 1
for number in range_of_numbers:
    product *= number
print(product)
