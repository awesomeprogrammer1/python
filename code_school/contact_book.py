from easygui import *
dict = {}
interface = buttonbox('Choose to function', 'Contact Book', ['add', 'remove', 'edit', 'search'])
print(interface)
if interface == 'add':
    contact_info = multenterbox('Please Enter Contact Information ', 'Contact', ['name','phone number'])
    dict[contact_info[0]] = contact_info[1]
    print(dict)