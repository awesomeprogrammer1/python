"""
The sequence consists of strings.
Determine the length of the longest element and return its index.
If there are several largest elements, output the index of the first one.

You can not use the following:
max()
index()

"""


def largest_element_index(lst: list) -> int:
    longest_elem = __largest_element(lst)
    for i in range(len(lst)):
        if lst[i] == longest_elem:
            return i


def __largest_element(lst: list) -> str:
    if len(lst) == 0:
        raise ValueError("List can't be empty")
    longest_element = lst[0]
    for i in range(1, len(lst)):
        if len(lst[i]) > len(longest_element):
            longest_element = lst[i]
    return longest_element
