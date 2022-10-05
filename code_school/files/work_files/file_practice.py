import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
path2 = os.path.join("code_school\\files\work_files", "test1.txt")
file_write = open(path, "w")
file_read = open(path, "r")
# task 1
dict_of_words = {}
words = ["greeting", "replenish", "attentive", "interesting", "boring"]
for word in words:
    if len(word) >= 7:
        dict_of_words[word] = len(word)
json.dump(dict_of_words, file_write)
file_write.close()
# task 2
number_of_line_in_file = 0
lines_in_file: list = []
print_lines_in_file: dict = {}
python_file = os.path.join("code_school\\files\work_files", "file_practice.py")
python_read = open(python_file, "r")
lines = python_read.readlines()
for line in lines:
    seperate_lines = line.split("\n")
    current_line = seperate_lines[0]
    path2 = os.path.join("code_school\\files\work_files", "test1.txt")
    write_in_txt = open(path2, "w")
    lines_in_file.append(current_line)
print(lines_in_file)
spaced_out_lines = " \n".join(lines_in_file)
print(spaced_out_lines)
write_in_txt.write(spaced_out_lines)
write_in_txt.close()
# task 3
write_in_txt = open(path2, "w")
lines_in_file.reverse()
spaced_out_lines = " \n".join(lines_in_file)
print(spaced_out_lines)
write_in_txt.write(spaced_out_lines)
write_in_txt.close()


# write_in_txt.write(spaced_out_lines[::-1])
# write_in_txt.close()

