# def get_number():
#     yield 1
#     yield 2
#     yield 3


# iter_obj = get_number()
# for i in range(2):
#     print(next(iter_obj))

list_var = [1, 2, 3, 4]
iter_obj = iter(list_var)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
