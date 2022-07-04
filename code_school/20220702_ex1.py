import time

# homework
# 1) count down instead of up when we lock the account
# 2) increase the lock time if we keep providing wrong information

mail = "admin@admin.com"
password = "qwerty12345"
login_errors = 1
lock_time = 10
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
        else:
            print("Error Code 421: Mail incorrect")
        login_errors += 1
    print("Account locked temporarily")
    for i in range(lock_time, 0, -1):
        print(i)
        time.sleep(1)
    print("Account Unlocked")
    lock_time += 5