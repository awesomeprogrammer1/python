list_var = [12, 34, 25, 15, 67, 23, 11, 5, 86]


def BubbleSort(lst):
    myList = list(lst)
    count = 0
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            count += 1
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

    print(f"Amount of times the program has run: {count}")
    return myList


print(list_var)
print(BubbleSort(list_var))
print(list_var)
