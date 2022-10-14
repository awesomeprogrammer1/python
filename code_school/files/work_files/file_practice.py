import os.path

path = os.path.join("code_school\\files\work_files", "test1.txt")
file_write = open(path, "w")
file_read = open(path, "r")
# task 1
words = ["greeting", "replenish", "attentive", "interesting", "boring"]
for word in words:
    if len(word) >= 7:
        file_write.write(word)
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

# task 4 (TBD)
file_read = open(path, "r")
file_write = open(path, "w")
for line in file_read:
    if "." not in line:
        spaced_out_lines = " \n************\n".join(lines_in_file)
        print(spaced_out_lines)
file_write.write(spaced_out_lines)
file_write.close()
file_read.close()

# task 5
character = input(
    "Input a random character and we will calculate how many times it is in the file: "
)
print(spaced_out_lines.count(character))

# task 6

# task 7

# task 8

# task 9
print(len(spaced_out_lines))
# task 10
file_read = open(path, "r")
lines = file_read.readlines()
print(len(lines))
