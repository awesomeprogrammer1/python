'''
Task 4
The user enters file names until they enter the word "quit".
After the input completes, the program must write words present in all listed files
to the final file (each file must contain words)
'''

def get_unique_words(file_name: str) -> set:
    file1_path = folder_with_info / file_name
    file_read = open(file1_path, "r")
    file_words = file_read.read().split()
    file_read.close()
    words = set(file_words)
    return words


from pathlib import Path
import os.path
base_set: set = {}
folder_with_info = Path("code_school/files/work_files")
given_file = input("Enter a file name ")
given_file += ".txt"
file1_path = folder_with_info / given_file
file_read = open(file1_path, "r")
file_words = file_read.read().split()
file_read.close()
for word in file_words:
    base_set.add(word)
while True:
    given_file = input("Enter a file name or quit to stop entering file names: ")
    given_file += ".txt"
    if given_file == "quit":
        break
    file1_path = folder_with_info / given_file
    file_read = open(file1_path, "r")
    file_words = file_read.read().split()
    file_read.close()
    set_words_in_file = set(file_words)
    set_words_in_file.intersection_update(base_set)
    print(set_words_in_file)
