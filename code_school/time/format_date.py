import time


def formatted_date(func):
    def inner():
        return time.strftime("%d-%m-%Y %I:%M %p UTC", time.gmtime(func()))

    return inner


@formatted_date
def my_birthday():
    return 1664582400


@formatted_date
def dads_birthday():
    return 1663891200


print(my_birthday())
print(dads_birthday())
