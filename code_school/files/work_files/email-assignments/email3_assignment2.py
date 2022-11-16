"""
Task 2: A menu with the following items
is displayed when the program starts:
1: Loading Data
2: Saving Data
3: Adding data
4: Deleting data
Use a list of integers as data storage.
Use Packing/Unpacking
"""
from pathlib import Path
from easygui import *
import os.path

path_hub = Path("code_school\\files\work_files")
path = path_hub / "email3_assignment2_output.txt"
path1 = path_hub / "email3_assignment2_output.txt"
from pathlib import Path

base_list = []


while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Contact Book",
        ["Load Data", "Save Data", "Add Data", "Delete Data", "exit"],
    )
    if interface == "Load Data":
        file1 = open(path, "r", encoding="utf8")
        load_file = file1.read()
        textbox("File Successfully Loaded", "Load File", load_file)
        file1.close()
    if interface == "Save Data":
        file1 = open(path, "r", encoding="utf8")
        save_file = file1.read()
        textbox("File Saved", "Save File", save_file)
        file1.close()
    if interface == "Add Data":
        file1 = open(path, "r", encoding="utf8")
        add_to_file = file1.readlines()
        file2 = open(path, "w", encoding="utf8")
        add_value = enterbox("Please enter an integer", "Add Data")
        add_to_file.append(add_value)
        add_int = " ".join(add_to_file)
        file2.write(add_int)
        file1.close()
        file2.close()
    if interface == "Delete Data":
        file1 = open(path, "r", encoding="utf8")
        remove_from_file = file1.read().split()
        file2 = open(path, "w", encoding="utf8")
        remove_int = enterbox("Please enter an integer to remove ", "Remove Data")
        if remove_int in remove_from_file:
            remove_from_file.pop(remove_from_file.index(remove_int))
        new_list = " ".join(remove_from_file)
        textbox("Element Successfully Deleted", "Delete Integer", new_list)
        file2.write(new_list)
        file1.close()
        file2.close()
    if interface == "exit":
        break

