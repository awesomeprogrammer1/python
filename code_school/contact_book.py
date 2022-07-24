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
    if interface == "add":
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        dict[contact_info[0]] = contact_info[1]
        textbox(dict)
        interface = ""
    if interface == "remove":
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
    if interface == "edit":
        edit_contact = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        if edit_contact not in dict:
            textbox("Error, Contact Does Not Exist.")
            interface = ""
        else:
            new_contact = multenterbox(
                "Please Edit The Existing Contact Info",
                "Edit Contact",
                ["name", "phone number"],
            )
            dict.pop(edit_contact)
            dict[new_contact[0]] = new_contact[1]
            textbox(dict)
            interface = ""
    if interface == "search":
        search_contact = enterbox(
            "Enter the Name of the Contact That You Would Like To Search",
            "Search Contact",
        )
        if search_contact not in dict:
            textbox("Error: Contact Does Not Exist")
            interface = ""
        else:
            textbox(dict[search_contact], "Andrews Number:")
            interface = ""
    if interface == "exit":
        textbox('Hit "OK" to close the Contact Book')
        exit()
