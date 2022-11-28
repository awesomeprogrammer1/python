"""
Task 4
The user enters file names until they enter the word "quit".
After the input completes, the program must write words present in all listed files
to the final file (each file must contain words)
"""
from pathlib import Path

def get_unique_words(file_name: str) -> set:
    folder_with_info = Path("code_school/files/work_files")
    file1_path = folder_with_info / file_name
    file_read = open(file1_path, "r")
    file_words = file_read.read().split()
    file_read.close()
    words = set(file_words)

    return words



base_set: set = set()
given_file = input("Enter a file name ")
given_file += ".txt"
for word in get_unique_words(given_file):
    base_set.add(word)
while True:
    given_file = input("Enter a file name or quit. to stop entering file names: ")
    if given_file == "quit.":
        break
    else:
        given_file += ".txt"
        base_set.intersection_update(get_unique_words(given_file))
print(base_set)
words_in_all_files = "".join(base_set)
folder_with_info = Path("code_school/files/work_files")
word_dump = folder_with_info / "email5_assignment4_output.txt"
file_write = open(word_dump, "w")
file_write.write(words_in_all_files)
file_write.close()
