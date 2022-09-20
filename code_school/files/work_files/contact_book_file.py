import os.path
from easygui import *


path = os.path.join("code_school\\files\work_files", "contact_book_list.txt")
file_obj = open(path, "w")

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
        file_obj.write()
    elif interface == "remove":
        remove_contact = enterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
        )
        if remove_contact not in dict:
            textbox("Error: Contact does not Exist, please try again ")
        else:
            dict.pop(remove_contact)
            textbox(dict)
    elif interface == "edit":
        contact_name = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        if contact_name not in dict:
            textbox("Error, Contact Does Not Exist.")
        else:
            contact_phone_number = enterbox(
                "Please Edit The Existing Phone Number",
                "Edit Contact",
            )

            dict[contact_name] = contact_phone_number
            textbox(dict)
    elif interface == "search":
        search_contact = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        if search_contact not in dict:
            textbox("Error: Contact Does Not Exist")
        else:
            textbox(dict[search_contact], "Users Phone Number")
    elif interface == "exit":
        exit()


# Name: Max, number: 08954367
