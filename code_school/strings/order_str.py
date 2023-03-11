'''
At the input we have a list of strings of different lengths.
You need to write a function all_eq(lst) that will return a new list of strings of the same length.
The length of the final line is determined based on the largest of them.
If a particular string is shorter than the longest one, pad it with underscores from the right edge to the required number of characters.
Do not change the location of the elements of the initial list


Test cases:
print(all_eq(['крот', 'белка', 'выхухоль']))
print(all_eq(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
Results:
['крот____', 'белка___', 'выхухоль']
['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

'''

# 1st variant


# def order_str(list_var: list) -> list:
#     longest_element = 0
#     for element in list_var:
#         if len(element) > longest_element:
#             longest_element = len(element)
#     for element in list_var:
#         orig_element = element
#         if len(element) < longest_element:
#             for i in range(longest_element-len(element)):
#                 element += "_"
#             list_var[list_var.index(orig_element)] = element
#     new_list = list_var
#     return new_list



def order_str(list_var: list) -> list:
    # longest_element = max(list_var)
    longest_element = max([len(element) for element in list_var]) 
    for element in list_var:
        orig_element = element
        if len(element) < longest_element:
            for i in range(longest_element-len(element)):
                element += "_"
            list_var[list_var.index(orig_element)] = element
    new_list = list_var
    return new_list


print(order_str(['крот', 'белка', 'выхухоль']))
print(order_str(['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
print(order_str(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))
