"""
Task 1: The user types in a list of integers.
Pack the recieved data and save  it to a file.
After that, upload the data from the file to a new list.
"""
from pathlib import Path
import os.path

path1 = os.path.join("code_school\\files\work_files", "email3_assignment1_output.txt")
path2 = os.path.join("code_school\\files\work_files", "email3_assignment1_output.txt")

file1 = open(path2, "w", encoding="utf8")
file2 = open(path1, "r", encoding="utf8")

list_of_int = input("Input a list of integers: ")
new_list_of_int = []
file1.write(list_of_int)
file1.close()
saved_data = file2.read()
for char in saved_data:
    new_list_of_int.append(char)
print(new_list_of_int)
file2.close()
