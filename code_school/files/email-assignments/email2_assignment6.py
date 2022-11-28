"""
Task 6 You have a text file.
Find and replace the specified word.
The user determines what to search for and to what it should be replaced.
"""
from pathlib import Path
import os.path

path_hub = Path("code_school\\files\work_files")
path1 = path_hub /  "assignment1.txt"
path2 = path_hub / "sample_text.txt"

file1 = open(path1, "r", encoding="utf8")
file2 = open(path2, "w", encoding="utf8")

replace_word = input("Enter a word that needs to be replaced: ")
new_word = input("Enter a word that will be replaced with the word you just inputted: ")
words = file1.read().split(" ")
for word in words:
    if replace_word in word:
        words[words.index(word)] = new_word
new_txt = " ".join(words)
file2.write(new_txt)
file1.close()
file2.close()
