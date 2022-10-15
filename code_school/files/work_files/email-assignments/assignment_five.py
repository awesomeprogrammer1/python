import os.path

path_load = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")
file = open(path_load, "r")
read_file = file.read().lower()
words = read_file.split()
counter = 0
given_character = input("Enter a character to look for in the file ").lower()
for i in range(len(words)):
    if given_character == words[i][0]:
        counter += 1
print(
    f"Character Given: {given_character} Amount of times the character was in the beginning of a element: {counter}"
)
