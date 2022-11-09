import os.path
'''
Task 6
You have a text file. Write all its lines to another file while replacing * with & and vice versa.
'''

path_load = os.path.join("code_school\\files\work_files", "random_symbols.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")

read_in_file = open(path_load, "r")
write_in_file = open(path_write, "w")
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
