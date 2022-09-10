from datetime import date
import time
from datetime import datetime


def formatted_date(func):
    def inner(date_time):
        print("I am going to format the date")
        print(time.strftime("%Y-%m-%d, %I:%M %p UTC", time.gmtime(date_time)))

    return inner


@formatted_date
def format_date(date_time):
    print(date_time)


format_date(3600)
