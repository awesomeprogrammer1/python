from easygui import *

dict = {}
interface = buttonbox(
    "Choose to function", "Contact Book", ["add", "remove", "edit", "search", "exit"]
)
while True:
    if interface == "":
        interface = buttonbox(
            "Choose to function", "Contact Book", ["add", "remove", "edit", "search", "exit"]
        )
    if interface == "add":
        contact_info = multenterbox(
            "Please Enter Contact Information ", "Add Contact", ["name", "phone number"]
        )
        dict[contact_info[0]] = contact_info[1]
        print(dict)
        interface = ""
    if interface == "remove":
        remove_contact = multenterbox(
            "Please Enter The Name of the Contact ",
            "Remove Contact",
            ["name", "phone number (optional)"],
        )
        if remove_contact[0] not in dict:
            print("Error: Contact does not Exist, please try again ")
            interface = ""
        else:
            dict.pop(remove_contact[0])
            print(dict)
            interface = ""
    if interface == "edit":
        edit_contact = enterbox(
            "Please Enter The Name Of The Contact You Would Like To Edit ",
            "Edit Contact",
        )
        if edit_contact not in dict:
            print('Error, Contact Does Not Exist.')
            interface = ''
        else: 
            new_contact = multenterbox('Please Enter The New Contact Info', 'Edit Contact', ["name", "phone number"])
            dict.pop(edit_contact)
            dict[new_contact[0]] = new_contact[1]
            print(dict)
            interface = ''
    if interface == "search":
        search_contact = enterbox('Enter the Name of the Contact That You Would Like To Search', 'Search Contact')
        if search_contact not in dict:
            print('Error: Contact Does Not Exist')
            interface = ''
        else:
            print('Andrews Number:', dict[search_contact])
            interface = ''
    if interface == "exit":
        print('Closing the Contact Book')
        exit()
        

       
