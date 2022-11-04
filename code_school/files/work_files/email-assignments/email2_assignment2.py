"""
Task 2: You have a text file.
Create a new file and write the following statistics
based on the source file to it:
■ Number of characters; ■ Number of lines; ■ Number of vowels;
■ Number of consonants; ■ Number of digits.
"""

import os.path

path1 = os.path.join("code_school\\files\work_files", "assignment1.txt")
path2 = os.path.join("code_school\\files\work_files", "email2_assignment2_output.txt")

file1 = open(path1, "r", encoding="utf8")
file2 = open(path2, "w", encoding="utf8")

vowels = ["a", "e", "i", "o", "u"]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count_vowels = 0
count_consonants = 0
count_digits = 0
file_read_var = file1.read()
file1.close()
for letter in file_read_var.split():
    if letter in vowels:
        count_vowels += 1
    elif letter != ' ':
        count_consonants += 1


for number in file_read_var:
    if number in digits:
        count_digits += 1


for number in file_read_var:
    if number in digits:
        count_digits += 1
no_of_lines = len(file_read_var.split("\n"))

file2.write(f"Number of Characters: {len(file_read_var )}")
file2.write("\n")
file2.write(f"Number of Lines: {no_of_lines}")
file2.write("\n")
file2.write(f"Number of Vowels: {count_vowels}")
file2.write("\n")
file2.write(f"Number of Consonants: {count_consonants}")
file2.write("\n")
file2.write(f"Number of Digits: {count_digits}")
file2.close()
