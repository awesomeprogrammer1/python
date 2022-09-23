import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")

dict_var = {}
dict_var["Hello"] = "Hi"
json.dump(dict_var, file)
file.close()

file2 = open(path, "r")
dict_var2 = json.load(file2)
print(dict_var2)
file.close()
