import time

# homework
# 1) count down instead of up when we lock the account
# 2) increase the lock time if we keep providing wrong information

mail = "admin@admin.com"
password = "qwerty12345"
extra_seconds = 1
place_holder = -10
while True:
    for i in range(5):
        user_mail = input("What is your email? ")
        user_password = input("What is your password? ")
        if user_mail == mail:
            if user_password == password:
                print("Welcome")
                exit()
            else:
                print("Error Code 278: Password incorrect")
                extra_seconds = extra_seconds + 1
        else:
            print("Error Code 421: Mail incorrect")
            extra_seconds = extra_seconds + 1
        if extra_seconds >= 10:
            place_holder = place_holder - 5
    print("Account locked temporarily")
    for i in range(place_holder, 0):
        print(-i)
        time.sleep(1)
        place_holder = place_holder
        extra_seconds = extra_seconds
    print("Account Unlocked")
