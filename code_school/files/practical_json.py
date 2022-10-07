import os.path
import json

number_list = []
path = os.path.join("code_school\\files\json_files", "test1.json")
file_write = open(path, "w")
number_input = input("Input a series of numbers seperated by spaces: ")
numbers = number_input.split(" ")
for i in range(len(numbers)):
    number_list.append(int(numbers[i]))
json.dump(number_list, file_write)
file_write.close()

file_read = open(path, "r")
file_contents = json.load(file_read)
print(sum(file_contents))
