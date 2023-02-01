list_var = [34, 19, 96, 2, 43, 64, 95, 75, 23]


def BubbleSort(lst):
    myList = list(lst)
    count = 0
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            count += 1
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

    print(count)
    return myList


print(list_var)
print(BubbleSort(list_var))
print(list_var)
