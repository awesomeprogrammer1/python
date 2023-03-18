"""
Petya moved to another school.
In a physical education lesson, he needed to determine his place in the ranks. Help him do it.
The program receives as input a non-increasing sequence of natural numbers,
meaning the growth of each person in the ranks.
After that, the number X is entered - Petya's height.
All numbers in the input are natural and do not exceed 200.
Print the number under which Petya should join the ranks. 
If there are people in the ranks with the same height, the same as Petya, then he must stand up after them.




"""


def ranks(student_heights: list, height: int) -> int:
    student_ranks = list(student_heights)
    student_ranks.append(height)
    sorted_heights = __sort_ranks(student_ranks)
    if sorted_heights.count(height) > 1:
        return sorted_heights.index(height) + sorted_heights.count(height)-1
    else:
        return sorted_heights.index(height)


def __sort_ranks(lst: list) -> list:
    new_list = list(lst)
    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - i - 1):
            if new_list[j] < new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list
    


