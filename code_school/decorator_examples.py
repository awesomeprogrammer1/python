# As stated above the decorators are used to modify the behaviour
# of function or class.
# In Decorators, functions are taken as the argument into another function
# and then called inside the wrapper function.


def hello_decorator1(func):

    # inner1 is a Wrapper function in
    # which the argument is called
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
        # calling the actual function now
        # inside the wrapper function.
        func()
        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator1(function_to_be_used)


# calling the function
function_to_be_used()


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


# 400 will be returned
print(num())

# <class 'function'>
print(type(num))
