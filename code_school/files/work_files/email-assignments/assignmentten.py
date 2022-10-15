import os.path


path_read = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")

file = open(path_read, "r")

lines = file.readlines()
print(len(lines))
file.close()
