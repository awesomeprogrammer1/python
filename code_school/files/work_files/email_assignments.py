import os.path
# Assignment 3

path_read = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")

file = open(path_read, "r")
file2 = open(path_write, "w")

lines = file.readlines()
lines.reverse()
joined_lines = "".join(lines)
file2.write(joined_lines)
file.close()
file2.close()


