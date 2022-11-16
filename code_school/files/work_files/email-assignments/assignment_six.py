import os.path
from pathlib import Path
'''
Task 6
You have a text file. Write all its lines to another file while replacing * with & and vice versa.
'''

path_load = Path("code_school\\files\work_files")
path_load_2 = path_load / "random_symbols.txt"
path_write = Path("code_school\\files\work_files")
path_write_2 = path_write / "test1.txt"

read_in_file = open(path_load_2, "r")
write_in_file = open(path_write_2, "w")
char = read_in_file.read()
lines = read_in_file.readlines()
amount_of_elements = len(lines)
lines = char.split("\n")
# print(lines)

for line in lines:
    new_str = ""
    for element in line:
        if "*" in element:
            new_str += "&"
        elif "&" in element:
            new_str += "*"
        else:
            new_str += element
    orig_element = lines.index(line)
    lines[orig_element] = new_str
    #
read_in_file.close()
new_lines = "\n".join(lines)
write_in_file.write(new_lines)
write_in_file.close()

# for line in lines:
#     if "*" in line:
#         line.replace("*", "&")
#     if "&" in line:
#         line.replace("&", "*")
# read_in_file.close()
# write_in_file.write(lines)
# write_in_file.close()
