# from random import randint


# def get_set() -> set:
#     set_var = [i for i in range(100)]
#     set_var.pop(randint(0,99))
#     return set(set_var)


# def get_removed_number(number_set: set) -> set:
#     set_var = set([i for i in range(100)])
#     number_set.symmetric_difference_update(set_var)
#     return number_set


# number_set = get_set()
# print(number_set)
# print(get_removed_number(number_set))


# Return the common numbers in these 3 sets
set_1 = {3, 4, 5, 6, 20}
set_2 = {4, 6, 7, 8, 9}
set_3 = {5, 3, 8, 1}


difference_in_sets = set_1.symmetric_difference(set_2).symmetric_difference(set_3)
print(difference_in_sets)
