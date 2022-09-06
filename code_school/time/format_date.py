from datetime import date
import time


named_tuple = time.localtime()


def format_date(func):
    def inner(date_time):
        print("I am going to format the date")
        print(time.strftime("%Y-%m-%d, %I:%M %p %Z", date_time))

    return inner


@format_date
def get_date(date_time: tuple) -> tuple:
    print(date_time)


get_date(time.localtime())
