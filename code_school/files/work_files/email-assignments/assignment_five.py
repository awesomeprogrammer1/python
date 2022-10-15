import os.path
path_load = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")
file = open(path_load, "r")
read_file = file.read().lower()
given_character = input("Enter a character to look for in the file ").lower()
print(f"Character Given: {given_character} Amount of times the character was in the file: {read_file.count(given_character)}")