"""
Task 4: You have a text file
Print the longest line in it
"""
from pathlib import Path
import os.path

path_hub = Path("code_school\\files\work_files")
path1 = path_hub / "assignment1.txt"
read_file = open(path1, "r")
lines = read_file.readlines()
longest_line = ""
for i in range(len(lines)):
    if len(lines[i]) > len(longest_line):
        longest_line = lines[i]
print(f"Longest line in file: {longest_line}")
