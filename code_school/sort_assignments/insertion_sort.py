# Task 2 Write a program that sorts a list of integers using the insertion method.
def Insertion_Sort(lst: list):
    new_lst = list(lst)
    for num in range(1, len(new_lst)):
        current_elem = new_lst[num]
        position = num
        while position > 0 and new_lst[position - 1] > current_elem:
            new_lst[position] = new_lst[position]
            position -= 1
        new_lst[position] = current_elem
    return new_lst


cool_list = [85, 24, 7, 32, 1, 13, 76, 83]
print(Insertion_Sort(cool_list))
