import os.path

# Task 4
path = os.path.join("code_school\\files\work_files", "test1.txt")
file_obj = open(path, "r")

for line in file_obj:
    if "." not in line:
        