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


numbers = [465,34,9,6456,3452534,95,23,54,72]
print("Original list: {}".format(numbers))
ShellSort(numbers)
print("Sorted list: {}".format(numbers))
