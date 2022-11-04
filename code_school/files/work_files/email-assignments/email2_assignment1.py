"""
Task 1: You have two text files.
Find out if their lines match.
If they don’t, print the mismatched line from each file.
"""

import os.path

path1 = os.path.join("code_school\\files\work_files", "assignment1.txt")
path2 = os.path.join("code_school\\files\work_files", "test1.txt")

file1 = open(path1, "r", encoding="utf8")
file2 = open(path2, "r", encoding="utf8")

file1_lines = file1.readlines()
file2_lines = file2.readlines()

lines_to_check = 0
if len(file1_lines) > len(file2_lines):
    lines_to_check = len(file2_lines)
else:
    lines_to_check = len(file1_lines)


for i in range(lines_to_check):
    if file1_lines[i] != file2_lines[i]:
        print(f"1: {file1_lines[i]} \n2: {file2_lines[i]}")

file_no = 0
if len(file1_lines) > lines_to_check:
    file_no = 1
    extra_lines = file1_lines[lines_to_check:]
elif len(file2_lines) > lines_to_check:
    file_no = 2
    extra_lines = file2_lines[lines_to_check:]

for line in extra_lines:
    print(f"{file_no}: {line}")
