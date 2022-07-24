from easygui import *

dict = {}
interface = buttonbox(
    "What do you want to do? ",
    "Contact Book",
    ["add", "remove", "edit", "search", "exit"],
)
while True:
    if interface == "":
        interface = buttonbox(
            "Choose to function",
            "Contact Book",
            ["add", "remove", "edit", "search", "exit"],
        )
    elif interface == "add":
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        dict[contact_info[0]] = contact_info[1]
        textbox(dict)
        interface = ""
    elif interface == "remove":
        remove_contact = enterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
        )
        if remove_contact not in dict:
            textbox("Error: Contact does not Exist, please try again ")
            interface = ""
        else:
            dict.pop(remove_contact)
            textbox(dict)
            interface = ""
    elif interface == "edit":
        edit_contact = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        if edit_contact not in dict:
            textbox("Error, Contact Does Not Exist.")
            interface = ""
        else:
            new_contact = enterbox(
                "Please Edit The Existing Phone Number",
                "Edit Contact",
            )
            dict.pop(edit_contact)
            dict[edit_contact] = new_contact
            textbox(dict)
            interface = ""
    elif interface == "search":
        search_contact = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        if search_contact not in dict:
            textbox("Error: Contact Does Not Exist")
            interface = ""
        else:
            textbox(dict[search_contact], 'Users Phone Number')
            interface = ""
    elif interface == "exit":
        textbox('Hit "OK" to close the Contact Book')
        exit()
