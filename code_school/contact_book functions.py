'''
This is the wrong way to implement contact book with functions
'''
from easygui import *

dict = {}


def add_contact():
    try:
        dict[contact_info[0]] = contact_info[1]
        return textbox(dict)
    except TypeError:
        return textbox("Error: Please close to return to calculator")


def remove_contact():
    try:
        if removing_contact not in dict:
            return textbox("Error: Contact does not Exist, please try again ")
        else:
            dict.pop(remove_contact)
            return textbox(dict)
    except TypeError:
        return textbox("Error: Please close to return to calculator")


def edit_contact():
    if contact_name not in dict:
        return textbox("Error, Contact Does Not Exist.")
    else:
        contact_phone_number = enterbox(
            "Please Edit The Existing Phone Number",
            "Edit Contact",
        )
        dict[contact_name] = contact_phone_number
        return textbox(dict)


def search_contact():
    '''
    search contact dictionary search_contact = enterbox(
        "Enter the Name of the Contact That You Would Like To Search",
        "Search Contact",
    )
    '''
    if search_contact not in dict:
        return textbox("Error: Contact Does Not Exist")
    else:
        return textbox(dict[searching_contact], "Users Phone Number")


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
        add_contact()
    elif interface == "remove":
        removing_contact = enterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
        )
        remove_contact()
    elif interface == "edit":
        contact_name = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        edit_contact()
    elif interface == "search":
        searching_contact = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        search_contact()
    elif interface == "exit":
        exit()
