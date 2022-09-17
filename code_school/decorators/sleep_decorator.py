from time import sleep


def pause_program(func):
    def inner(a):
        print("I am going to stop the program for", a, "seconds")
        func(a)
        print("Program has resumed")

    return inner


@pause_program
def sleep_func(a: float):
    sleep(a)


sleep_func(2.4)
