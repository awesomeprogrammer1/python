import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")

dict_var = {}
for i in range(101):
    if i % 2 == 0:
        dict_var[i] = i * 2
json.dump(dict_var, file)
file.close()

file2 = open(path, "r")
dict_load = json.load(file2)

dict_sum = sum(dict_load.values())
print(dict_sum)
file2.close()
