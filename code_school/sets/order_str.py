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

def all_eq(list_var):
    longest_element = 0
    for element in list_var:
        if len(element) > longest_element:
            longest_element = len(element)
    for element in list_var:
        if len(element) < longest_element:
            for i in range(longest_element-len(element)):
                element += "_"
                


