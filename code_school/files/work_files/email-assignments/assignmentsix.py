import os.path

path_load = os.path.join("code_school\\files\work_files", "random_symbols.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")

read_in_file = open(path_load, "r")
write_in_file = open(path_write, "w")
char = read_in_file.read()
lines = read_in_file.readlines()
amount_of_lines = len(lines)
lines = char.split("\n")
# print(lines)

for line in lines:
    new_str = ""
    for element in line:
        if "*" in element:
            new_str += "&"
            continue
        if "&" in element:
            new_str += "*"
            continue
        else:
            new_str += element
            continue    
    if "*" in lines[0]:
        lines.pop(0)
        lines.append(new_str)
    #
print(lines)

# for line in lines:
#     if "*" in line:
#         line.replace("*", "&")
#     if "&" in line:
#         line.replace("&", "*")
# read_in_file.close()
# write_in_file.write(lines)
# write_in_file.close()
