"""
Task 5 You have a text file.
Count how many times the word specified by the user occurs in it.
"""


import os.path

path1 = os.path.join("code_school\\files\work_files", "assignment1.txt")
read_file = open(path1, "r")
file_content = read_file.read()
specific_word = input("Input a random word to calculate how many times it appears in the text file ")
print(file_content.count(specific_word))
