import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")
# indicate we want to write
# in the file

dict_var: dict = {}
# creating new dict
dict_var["Hello"] = "Hi"
# adding new key-value pair to dict
json.dump(dict_var, file)
# convert dict to json
# and put it into json file
file.close()
# close file

file2 = open(path, "r")
# indicate that we want to read the file
dict_var2 = json.load(file2)
# loads the contents of the json file
# into the program
print(dict_var2)
# prints the contents of whatever
# we got from the json file
file.close()
# closes the file
