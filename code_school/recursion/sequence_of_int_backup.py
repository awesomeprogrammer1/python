"You have a list of integers that ends with the number 0"

"Return the same list in reverse order, using recursion"



def sequence_of_int(lst: list[int]) -> list:
    current_elem = lst.pop(lst.index(0)-1)
    lst.append(current_elem)
    if 0 == lst[0]:
        return lst
    else:
        return sequence_of_int(lst)
    
print(sequence_of_int([4,8,9,0]))

