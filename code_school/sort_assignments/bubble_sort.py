# cool_list = [5, 17, 9, 92, 45, 107]
# for i in range(len(cool_list) - 1):
#     print(cool_list[i], cool_list[i + 1])
#     if cool_list[i] > cool_list[i + 1]:
#         cool_list[i], cool_list[i + 1] = cool_list[i + 1], cool_list[i]
# print(cool_list)


# myList = [5, 17, 9, 92, 45, 107]
# for i in range(len(myList) - 1):
#     for j in range(len(myList) - 1):
#         if myList[j] < myList[j + 1]:
#             myList[j], myList[j + 1] = myList[j + 1], myList[j]
# print(myList)


# [17, 9, 92, 45, 107, 5]

# Email assignment 3:
myList = [5, 17, 9, 92, 45, 107]
myListIndex = len(myList) / 2
myList1 = myList[int(myListIndex):]
myList2 = myList[: int(myListIndex)]
# Task 3 There is a list of integers.
# It is necessary to sort the first half of the list in descending order,
# the second half in ascending order.


def BubbleSort_increase(lst):
    myList = list(lst)
    count = 0
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            count += 1
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList


def BubbleSort_decrease(lst):
    myList = list(lst)
    count = 0
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            count += 1
            if myList[j] < myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList



def BubbleSort_inc_dec(lst):
    for h in range()


main_list = BubbleSort_decrease(myList2) + (BubbleSort_increase(myList1))
print(BubbleSort_increase(myList1))
print(BubbleSort_decrease(myList2))
print(main_list)
