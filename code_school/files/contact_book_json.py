import os.path
from easygui import *
import json


path = os.path.join("code_school\\files\json_files", "test1.json")
file = open(path, "w")

dict_var = {}

while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Contact Book",
        ["add", "remove", "edit", "search", "exit"],
    )
    if interface == "add":
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        dict_var[contact_info[0]] = contact_info[1]
        json.dump(dict_var, file)
        file.close()
