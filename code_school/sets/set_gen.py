'''
A list of natural numbers is provided. 
It is required to form a set of them. 
If any number is repeated, then convert it to a string according to the pattern: 
for example, if the number 4 is repeated 3 times, then the following entry will be in the set: 
the number 4 itself, the string "44" (the second repetition, i.e. the number is duplicated in line),
the line "444" (the third repetition, i.e. the line is multiplied by 3). Implement set output via the set_gen() function.

(Tests for #3)
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))
----------------------------------------------------------------------------
Result:
{1, 3, '111', '33', '11'}
{'5555555', 5, '55', '55555', '5555', '555555', '555'}
{1, 2, 3, 5, 6, 7, '22', '2222', '22222', '222', '11', '222222'}

'''