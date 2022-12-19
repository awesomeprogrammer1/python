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


def write_results(result_set: set, file_name: str) -> None:
    words_in_all_files = " ".join(result_set)
    folder_with_info = Path("code_school/files/work_files")
    word_dump = folder_with_info / file_name
    file_write = open(word_dump, "w")
    file_write.write(words_in_all_files)
    file_write.close()


def main():
    given_file = input("Enter a file name ")
    base_set: set = get_unique_words(given_file)
    while True:
        given_file = input("Enter a file name or quit. to stop entering file names: ")
        if given_file == "quit.":
            break
        else:
            base_set.intersection_update(get_unique_words(given_file))
    print(base_set)
    write_results(base_set, "email5_assignment4_output.txt")


main()
