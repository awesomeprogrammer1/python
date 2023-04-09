"""
The sequence consists of natural numbers and ends with the number 0.
Determine the index of the largest element of the sequence.
If there are several largest elements, output the index of the first one.
Element numbering starts from zero.

You can not use the following:
max()
index()

"""




def max_index(lst: list) -> int:
    max_elem = __max_element(lst)
    for i in range(len(lst)):
        if lst[i] == max_elem:
            return i


def __max_element(lst: list) -> int:
    if len(lst) == 0:
        raise ValueError("List can't be empty")
    max_element = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    return max_element
