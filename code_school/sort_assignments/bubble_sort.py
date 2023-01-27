# cool_list = [5, 17, 9, 92, 45, 107]
# for i in range(len(cool_list) - 1):
#     print(cool_list[i], cool_list[i + 1])
#     if cool_list[i] > cool_list[i + 1]:
#         cool_list[i], cool_list[i + 1] = cool_list[i + 1], cool_list[i]
# print(cool_list)
myList = [5, 17, 9, 92, 45, 107]
for i in range(len(myList) - 1):
    for j in range(len(myList) - 1):
        if myList[j] < myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]
print(myList)
