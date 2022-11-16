'''
Task 10 You have a text file. Calculate the number of lines in it
'''
from pathlib import Path


path_read = Path("code_school\\files\work_files")
read_access = path_read / "assignment1.txt"


file = open(read_access, "r")

lines = file.readlines()
print(f"Number of lines in the file: {len(lines)}")
file.close()
