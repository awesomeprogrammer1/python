"""
Task 4: You have a text file
Print the longest line in it
"""
from pathlib import Path
import os.path

path1 = os.path.join("code_school\\files\work_files", "assignment1.txt")
read_file = open(path1, "r")
lines = read_file.readlines()
longest_line = ""
for i in range(len(lines)):
    if len(lines[i]) > len(longest_line):
        longest_line = lines[i]
print(f"Longest line in file: {longest_line}")
