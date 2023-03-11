def shell_sort(lst):
    gap = len(lst) // 2
    # gets the space between the elements that we are comparing

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


lst = [12, 34, 25, 15, 67, 23, 11, 86]
print("Original List:  ", lst)
result = shell_sort(lst)
print("Sorted List:  ", result)


# [465, 34, 9, 54, 3452534, 95, 23, 6456]
# [9, 23, 465, 3452534]
# [34, 54, 95, 6456]
# [9, 23, 34, 54, 95, 465, 6456, 3452534, 6456]