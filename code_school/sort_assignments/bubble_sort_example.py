def BubbbleSort(lst):
    new_list = list(lst)
    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - i - 1):
            if new_list[j] < new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list


cool_list = [5, 17, 9, 92, 45, 107]
print(cool_list)
print(BubbbleSort(cool_list))
print(cool_list)


def InsertionSort(lst):
    new_list = list(lst)
    for i in range(len(new_list)):
        while new_list[i] < new_list[i - 1]:
            object = new_list[i]
            new_list[i] = new_list[i - 1]
            new_list[i - 1] = object
    return new_list


print(InsertionSort(cool_list))
