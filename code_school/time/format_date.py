from datetime import date
import time
from datetime import datetime

seconds = input("Input in the format: 21 June, 2018 2:35 UTC: ")
named_tuple = time.localtime()


def format_date(func):
    def inner(date_time):
        print("I am going to format the date")
        date_object = datetime.strptime(date_time, "%d %B, %Y %H:%M UTC")
        print(date_object)

    return inner


@format_date
def get_date(date_time: str):
    print(date_time)


get_date(seconds)
