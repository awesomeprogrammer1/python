from datetime import date
import time

seconds = float(
    input(
        "Get the UTC date and time at a certain amount of seconds past the epoch. Format Example: 3600.0. Note: 1 hour is 3600.0 seconds and 1 day is 86400 seconds. 1 year is 31536000 seconds and 1 leap year is 31622400 seconds "
    )
)
named_tuple = time.localtime()


def format_date(func):
    def inner(date_time):
        print("I am going to format the date")
        print(time.strftime("%Y-%m-%d, %I:%M %p UTC", date_time))

    return inner


@format_date
def get_date(date_time: float):
    print(date_time)


fixed_seconds = time.gmtime(seconds)
get_date(fixed_seconds)
