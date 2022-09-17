'''
This is the right way to implement contact book with functions
'''
from easygui import *

contact_book = {}


def add_contact(name: str, phone: str) -> None:
    contact_book[name] = phone


def remove_contact(name: str) -> None:
    contact_book.pop(name)


def edit_contact(name: str, phone: str) -> None:
    if name in contact_book.keys():
        contact_book[name] = phone


def get_contact(name: str) -> str:
    return contact_book.get(name)


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
        add_contact(contact_info[0], contact_info[1])
        textbox(contact_book)
    elif interface == "remove":
        name = enterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
        )
        if get_contact(name):
            remove_contact(name)
        else:
            textbox("Error: Contact does not Exist, please try again ")
        textbox(contact_book)
    elif interface == "edit":
        name = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        if get_contact(name):
            phone_number = enterbox(
                "Please Edit The Existing Phone Number",
                "Edit Contact",
            )
            edit_contact(name, phone_number)
        else:
            textbox("Error, Contact Does Not Exist.")
        textbox(contact_book)
    elif interface == "search":
        name = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        contact_info = get_contact(name)
        if contact_info:
            textbox(contact_info, "Users Phone Number")
        else:
            textbox("Error: Contact Does Not Exist")
    elif interface == "exit":
        exit()
