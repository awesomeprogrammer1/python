"""
Task 3: There is a dictionary
that stores usernames and passwords.
A username is a key, and a password is a value.
Implement the following:
Adding, deleting, finding, editing, saving, and loading data
(Use packing and unpacking)
"""
from easygui import *
import json
import os.path
from pathlib import Path

path_hub = Path("code_school\\files\work_files")
path = path_hub / "email3_assignment3_output.json"


while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Contact Book",
        ["Add", "Delete", "Search", "Edit", "Save", "Load", "Exit"],
    )
    if interface == "Add":
        user_password_cmbo_load = open(path, "r")
        add_to_dict = json.load(user_password_cmbo_load)
        user_password_cmbo_load.close()
        add_user = multenterbox(
            "Please Enter User Information ", "Add User", ["Name", "Password"]
        )
        add_to_dict[add_user[0]] = add_user[1]
        user_password_cmbo_write = open(path, "w")
        json.dump(add_to_dict, user_password_cmbo_write)
        textbox("Added pair to dictionary", "Add New Pair")
        user_password_cmbo_write.close()
    if interface == "Delete":
        json_file_read = open(path, "r")
        access_dict = json.load(json_file_read)
        json_file_read.close()
        remove_user = enterbox(
            "Please Enter The Name of the User ",
            "Remove User",
        )
        if remove_user not in access_dict:
            textbox("Error: User does not Exist, please try again ")
        else:
            access_dict.pop(remove_user)
        user_password_cmbo_write = open(path, "w")
        access_dict_w = open(path, "w")
        json.dump(access_dict, access_dict_w)
        textbox("User Successfully Removed", "Remove User", access_dict)
        access_dict_w.close()
    if interface == "Search":
        json_file_read = open(path, "r")
        access_dict = json.load(json_file_read)
        search_user = enterbox(
            "Please Enter The Name of the User ",
            "Search User",
        )
        if search_user in access_dict.keys():
            textbox("Password of user:", "Search Contact", access_dict[search_user])
        json_file_read.close()
    if interface == "Edit":
        json_file_read = open(path, "r")
        access_dict = json.load(json_file_read)
        json_file_read.close()
        edit_user = enterbox(
            "Please Enter The Name of the User ",
            "Edit User",
        )
        if edit_user in access_dict.keys():
            new_pass = enterbox(
                "Enter the new password ",
                "Edit User",
            )
            access_dict[edit_user] = new_pass
        access_dict_w = open(path, "w")
        json.dump(access_dict, access_dict_w)
        textbox("Dict successfully edited")
        access_dict_w.close()
    if interface == "Save":
        json_file_read = open(path, "r")
        access_dict = json.load(json_file_read)
        textbox("Dictionary Saved Successfully.")
        access_dict.close()
    if interface == "Load":
        textbox("Error, dict already loaded and ready for operation")
    if interface == "Exit":
        break
