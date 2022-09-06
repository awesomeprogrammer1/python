from datetime import date
import time

seconds = float(input("Get the UTC date and time at a certain amount of seconds past the epoch. Format Example: 3600.0. Note: 1 hour is 3600.0 seconds "))
named_tuple = time.localtime()


def format_date(func):
    def inner(date_time):
        print("I am going to format the date")
        print(time.strftime("%Y-%m-%d, %I:%M %p UTC", date_time))

    return inner


@format_date
def get_date(date_time: tuple) -> tuple:
    print(date_time)


get_date(time.gmtime(seconds))
