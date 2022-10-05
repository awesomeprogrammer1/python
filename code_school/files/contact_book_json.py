import os.path
from easygui import *
import json


path = os.path.join("code_school\\files\json_files", "test1.json")



while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Contact Book",
        ["add", "remove", "edit", "search", "exit"],
    )
    if interface == "add":
        contact_book_file = open(path, "r")
        contact_book_dict = json.load(contact_book_file)
        contact_book_file.close()
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        contact_book_dict[contact_info[0]] = contact_info[1]
        contact_book_file = open(path, "w")
        json.dump(contact_book_dict, contact_book_file)
        contact_book_file.close()
