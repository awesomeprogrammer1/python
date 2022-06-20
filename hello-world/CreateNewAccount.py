users = [] # List
passwords = [] # List


def sign_in(login):
    password = input('Input your password \n') # Inputting password
    if password == passwords[users.index(login)]:
        print('Access to your account has been granted')
    else:
        print('Error 278: Password incorrect')
        sign_in(login)

def is_there_login_in_password(login, password):
    result = login in password # Is there login in password? (True/False)
    return result

# My dad created placeholder functions for me
def does_password_have_numbers(password): # Asking if there are numbers
    result = ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") in password #Checking for numbers (True/False)
    return result # Message to verify

def is_login_in_username_list(): 
    while True:
        new_login_name = input('What will be your login name? ')  # Asking for login name
        if new_login_name.lower() == 'stop': # Breaks the loop
            break
        if new_login_name in users: # Checking if there is already an existing login name
            sign_in(new_login_name)
            # Continue later
            continue # Restarts the loop
        else:
            while True:       # Infinite Loop
                new_password = input('What will be your new password? ') # Asking for password
                if len(new_password) < 8 or is_there_login_in_password(new_login_name, new_password) or not does_password_have_numbers(new_password):   # True/False + Checking if there are more than 8 characters, if the password is not a part of the login name, and checking if the password has numbers.
                    print('Error 528: Password or username is invalid') # Output response
                else:
                    break
            print('Sucessfully logged in') # Output response


while True: # Infinite Loop
   is_login_in_username_list()
   users.append(new_login_name) # Adds list of login names
   passwords.append(new_password) # Adds list of  login passwords
print(users) # Prints list of usernames
print(passwords) # Prints lists of passwords
# print(does_password_have_numbers("rursiuhfkjsd"))