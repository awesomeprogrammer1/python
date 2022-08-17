# assignment 1
# make a presentation
# about subject topic about strings
# and what you can do with them


x = lambda a: a + 10
print(x(5))


a = lambda a, b: a * b
print(a("hello", 3))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)


mytripler = myfunc(3)

print(type(mydoubler))
print(type(mydoubler(11)))
print(mydoubler(11))
print(mytripler(11))
