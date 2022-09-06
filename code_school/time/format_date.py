import time

named_tuple = time.localtime()


def format(func):
    def inner(a):
        print("I am going to format the date")
        return func(a)
    return inner


@format
def format_date(a):
    print(time.strftime("%Y-%m-%d, %I:%M %p %Z", a))


format_date(named_tuple)
