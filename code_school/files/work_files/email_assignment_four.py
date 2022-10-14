import os.path
from re import T
# Assignment 4

path_read = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")

input_file = open(path_read, "r")
output_file = open(path_write, "w")

# lines = input_file.readlines()
# lines.reverse()
# for line in lines:
#     if "," not in line:
#         lines[lines.index(line)] = line + "*"*12  # gets the index at where there is no "," and then replaces the line with the same line but with twelve asterysks added to the end of the line
#         break


# input_file.close()
# output_file.close()
previos_line_has_comma = False
for line in input_file:
    if "," in line:
        previos_line_has_comma = True
        continue
    else:
        
    if not found_comma:
        output_file.write("*"*12)
        found_comma = False

    output_file.write(line)




input_file.close()
output_file.close()