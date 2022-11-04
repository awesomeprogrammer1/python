import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")
# indicates we want to write
# in the file

dict_var = {}
# creating new dict
for i in range(101):
    # for loop to check numbers (the indexes)
    if i % 2 == 0:
        # checking if the given index is a positive or negative number
        dict_var[i] = i * 2
        # if so, it creates a new dictionary
        # with the number being the key
        # and the value being the key
        # multiplied by a factor of 2
json.dump(dict_var, file)
# puts the dictionary of even numbers in the json file
file.close()
# closes the file

file2 = open(path, "r")
# indicates we want to read in the file
dict_load = json.load(file2)
# loads file into program0

dict_sum = sum(dict_load.values())
print(dict_sum)
file2.close()
