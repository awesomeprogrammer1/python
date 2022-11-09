import os.path
'''
Task 5: You have a text file.
Calculate the number of words that begin with a character set by the user.
'''


path_load = os.path.join("code_school\\files\work_files", "assignment1.txt")
path_write = os.path.join("code_school\\files\work_files", "test1.txt")
file = open(path_load, "r")
words = file.read().split()
counter = 0
given_character = input("Enter a character to look for in the file ")
for i in range(len(words)):
    if given_character == words[i][0]:
        counter += 1
print(
    f"Number of words that start with '{given_character}': {counter}"
)
file.close()
