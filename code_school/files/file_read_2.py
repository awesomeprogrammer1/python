from io import TextIOWrapper
import os.path
from typing_extensions import LiteralString

path: LiteralString = os.path.join("code_school\\files\work_files", "test1.txt")

file: TextIOWrapper = open(path, "r")


for line in file:
    new_line: list = line.split()
    # splitting the line into parts so we can operate
    # on the numbers
    sum_var: int = 0
    # create new sum_var
    for element in new_line[1:]:
        element_int: int = int(element)
        # converts element from str to int
        sum_var += element_int
        # adds number at the given index
        # in element_int
        # to existing variable sum_var
    try:
        print(f"Name: {new_line[0]} Average: {round(sum_var/len(new_line[1:]))}")
    except IndexError:
        break
    # prints a formatted string with the name and average
    # of the numbers next to his/her name
    # if the for loop trys printing
    # a line that doesn't exist
    # the except statement ends the loop
