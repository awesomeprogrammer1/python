from easygui import *

dict = {}


def add_contact(interface_choice):
    if interface_choice == "add":
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        dict[contact_info[0]] = contact_info[1]
        return textbox(dict)


def remove_contact(interface_choice):
    if interface_choice == "remove":
        remove_contact = enterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
        )
        if remove_contact not in dict:
            return textbox("Error: Contact does not Exist, please try again ")
        else:
            dict.pop(remove_contact)
            return textbox(dict)


def edit_contact(interface_choice):
    if interface_choice == "edit":
        contact_name = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
    if contact_name not in dict:
        return textbox("Error, Contact Does Not Exist.")
    else:
        contact_phone_number = enterbox(
            "Please Edit The Existing Phone Number",
            "Edit Contact",
        )
        dict[contact_name] = contact_phone_number
        return textbox(dict)


def search_contact(interface_choice):
    if interface_choice == "search":
        search_contact = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        if search_contact not in dict:
            return textbox("Error: Contact Does Not Exist")
        else:
            return textbox(dict[search_contact], "Users Phone Number")


while True:
    interface = buttonbox(
        "What do you want to do? ",
        "Contact Book",
        ["add", "remove", "edit", "search", "exit"],
    )
    if interface == "add":
        add_contact("add")
    elif interface == "remove":
        remove_contact("remove")
    elif interface == "edit":
        edit_contact("edit")
    elif interface == "search":
        search_contact("search")
    elif interface == "exit":
        exit()
