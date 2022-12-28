"""
A list of natural numbers is provided. 
It is required to form a set of them. 
If any number is repeated, then convert it to a string according to the pattern:
for example, if the number 4 is repeated 3 times, then the following entry will be in the set:
the number 4 itself, the string "44" (the second repetition, i.e. the number is duplicated in line),
the line "444" (the third repetition, i.e. the line is multiplied by 3). Implement set output via the set_gen() function.

Tests:
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

"""


def set_gen(list: list) -> set:
    set_var = set(list)
    base_set: set = set()
    for number in set_var:
        number_as_str = str(number)
        count_num = list.count(number)
        if count_num > 1:
            if count_num <= 2:
                number_as_str += number_as_str
                base_set.add(number_as_str)
            else:
                new_num_as_str = number_as_str + number_as_str
                base_set.add(new_num_as_str)
                for i in range(count_num - 2):
                    new_num_as_str += number_as_str
                    base_set.add(new_num_as_str)
    set_var.symmetric_difference_update(base_set)
    return set_var


list_1 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
