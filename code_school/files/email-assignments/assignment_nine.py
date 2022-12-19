'''
Task 9 You have a text file. Calculate the number of characters in it.
'''
import os.path
from pathlib import Path

path_read = Path("code_school\\files\work_files")
path_to_file = path_read / "assignment1.txt"

file = open(path_to_file, "r")

characters_in_file = file.read()
print(f"Characters in the file: {len(characters_in_file)}")
file.close()
