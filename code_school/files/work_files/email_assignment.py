import os.path

# Assignment 1
path_load = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")
file = open(path_load, "r")
file2 = open(path_write, "w")
read_var = file.read().split()
for word in read_var:
    if len(word) > 7:
        file2.write(word + " ")
file.close()
file2.close()
# Assignment 2
path_load = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")
file_read = open(path_load, "r")
file_write = open(path_write, "w")
lines = file_read.read()
file_write.write(lines)
file_read.close()
file_write.close()
# Assignment 3

