from datetime import date
from multiprocessing.sharedctypes import Value
import time
from datetime import datetime

seconds = input("Input in the format: 21 June, 2018 2:35 UTC: ")
named_tuple = time.localtime()


def format_date(func):
    def inner(date_time):
        try:
            print("I am going to format the date")
            date_object = datetime.strptime(date_time, "%d %B, %Y %H:%M UTC")
            print(date_object)
        except ValueError:
            print("Error, invalid format. You entered", func(date_time))
    return inner


@format_date
def get_date(date_time: str):
    print(date_time)


get_date(seconds)
