'''
Given a list of numbers. 
Determine how many elements in this list 
that are greater than two of their neighbors,
and output the number of such elements. 
The outermost elements of the list are never counted because they don't have enough neighbors.


'''



def list_neighbours(lst: list) -> int:
    counter = 0
    if len(lst) > 2:
        for i in range(1, len(lst)-1):
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                counter += 1
    return counter