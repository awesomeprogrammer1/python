"""
Task 3 You have a text file.
Delete the last line from it.
Write the result to another file.
"""
from pathlib import Path
import os.path

path1 = os.path.join("code_school\\files\work_files", "assignment1.txt")
path2 = os.path.join("code_school\\files\work_files", "email2_assignment3_output.txt")

file1 = open(path1, "r", encoding="utf8")
file2 = open(path2, "w", encoding="utf8")

lines = file1.readlines()


lines.pop()
result = "".join(lines)
file2.write(result)
file1.close()
file2.close()

