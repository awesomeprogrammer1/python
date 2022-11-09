'''
Task 4 The user enters file names until he or she enters the word “quit.”
After the input completes, the program must write characters present
in all listed files to the final file (each file must contain characters).
'''
import os.path
from pathlib import Path
folder_with_info = Path("code_school/files/work_files")

base_list = []
while True:
    try:
        given_file = input("Enter a file name or quit to stop entering file names: ")
        if given_file == "quit.":
            break
        user_given_file = os.path.join("code_school\\files\work_files", given_file + ".txt")
        sample_text = open(user_given_file, "r")
        current_file = sample_text.read()
        sample_text.close()
        base_list.append(current_file)
    except FileNotFoundError:
        print("Error, file does not exist, please retry")
        