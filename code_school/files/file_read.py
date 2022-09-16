import os.path

path = os.path.join("code_school\\files\work_files", "test1.txt")

file = open(path, "r")
# read_var = file.read()
# print(read_var)
# for line in file:
#     print(line)
# file.close()

name_var = input("What is the name of the student? ").lower()
for line in file:
    new_line = line.split()
    if name_var == new_line[0]:
        print(new_line[1])
        break
else:
    print("Error, user does not exist")
file.close()
