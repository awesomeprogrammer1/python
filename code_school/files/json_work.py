import os.path
import json

path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")

sentence = input("Enter a sentence ")
dict_var: dict = {}
sentence_words = sentence.split()


for word in sentence_words:
    dict_var[word] = sentence_words.count(word)
json.dump(dict_var, file)
file.close()

file2 = open(path, "r")
dict_load = json.load(file2)
for element in dict_load:
    if dict_load[element] == 2:
        print(element)
file2.close()
