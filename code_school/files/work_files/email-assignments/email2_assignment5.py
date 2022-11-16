"""
Task 5 You have a text file.
Count how many times the word specified by the user occurs in it.
"""

from pathlib import Path
import os.path

path_hub = Path("code_school\\files\work_files")
path1 = path_hub / "assignment1.txt"
read_file = open(path1, "r")
file_content = read_file.read()
specific_word = input("Input a random word to calculate how many times it appears in the text file ")
print(file_content.count(specific_word))
