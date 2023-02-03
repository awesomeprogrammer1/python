def ShellSort(myList):
    subListN = len(myList) // 2
    step = 1
    while subListN > 0:
        for startInd in range(subListN):
            InsertionSort(myList, startInd, subListN)
        print("Interval={}. After step {}: {}".format(subListN, step, myList))
        subListN = subListN // 2


def InsertionSort(myList, startInd, gapValue):
    for i in range(startInd + gapValue, len(myList), gapValue):
        currentElem = myList[i]
        currentInd = i
        while currentInd >= gapValue and myList[currentInd - gapValue] > currentElem:
            myList[currentInd] = myList[currentInd - gapValue]
            currentInd = currentInd - gapValue
        myList[currentInd] = currentElem


numbers = [12, 34, 25, 15, 67, 23, 11, 5, 86]
print("Original list: {}".format(numbers))
ShellSort(numbers)
print("Sorted list: {}".format(numbers))


# [465, 34, 9, 54, 3452534, 95, 23, 6456]
# [9, 23, 465, 3452534]
# [34, 54, 95, 6456]
# [9, 23, 34, 54, 95, 465, 6456, 3452534, 6456]