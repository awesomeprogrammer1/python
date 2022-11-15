"""
Task 3 The user enters file names until he or she enters the word “quit.”
After the input completes,
the program must combine the contents of all files listed by the user into one.
"""

import os.path
from pathlib import Path

base_str = ""
while True:
    try:
        given_file = input("Enter a file name or quit to stop entering file names: ")
        if given_file == "quit.":
            break
        user_given_file = os.path.join("code_school\\files\work_files", given_file + ".txt")
        sample_text = open(user_given_file, "r")
        current_file = sample_text.read()
        sample_text.close()
        base_str += current_file
        base_str += "\n"
    except FileNotFoundError:
        print("Error, file does not exist, please retry")

output = os.path.join("code_school\\files\work_files", "email5_assignment4_output.txt")
main_w = open(output, "w")
main_w.write(base_str)
main_w.close()
