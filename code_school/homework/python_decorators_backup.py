def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))

# make_pretty is the decorator in this scenario
# the decorator takes a function as a parameter
# which is then called inside the inner function


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


# ordinary function
def ordinary():
    print("I am ordinary")


ordinary()

pretty = make_pretty(ordinary)
pretty()


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)

    return inner


working_for_all = works_for_all(ordinary)
working_for_all()


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
