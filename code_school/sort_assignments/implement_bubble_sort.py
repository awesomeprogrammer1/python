list_var = [34, 19, 96, 2, 43, 64]


def BubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(BubbleSort(list_var))
