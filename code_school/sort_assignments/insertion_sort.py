# Task 2 Write a program that sorts a list of integers using the insertion method.
def Insertion_Sort(lst: list):
    new_lst = list(lst)
    # creates a new copy of the list
    for num in range(1, len(new_lst)):
        # creates a loop to sort all elemenets except the first one
        current_elem = new_lst[num]
        # appends the element we are currently comparing to a variable
        position = num
        # sets the index to which we are comparing so we can change ethe position of the elements
        while position > 0 and new_lst[position - 1] > current_elem:
            # checks if the position is not at 0 since 0 is deemed as already sorted
            # and that the element in front of the current element is greater/less 
            # depending if the list is being sorted in ascending/descending order
            new_lst[position] = new_lst[position]
            # confirms the position of the list
            position -= 1
            # lowers the number by one to change the position of the element
        new_lst[position] = current_elem
        # switches the elements
    return new_lst


cool_list = [85, 24, 7, 32, 1, 13, 76, 83]
print(Insertion_Sort(cool_list))
