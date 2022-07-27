# assignment 1:
# write the perimeter_area_rectangle function in one line
# assignment 2:
# write a program called "calculator" with the help of functions
# with plus, minus, multiply, and divide
# assignment 3:
# {"P":123,"A":123}
# create a version of perimeter_area_rectangle where
# the returned value is a dictionary and not a formatted string
# additionally, create a function called "print_perimeter_area_rectangle"
# and the function prints out the original formatted string
# assignment 4:
# learn about assert


# def math(a, b):
#     return a+b


# print(math(b=5, a=2)) #print(7)
# c = math(7,9)
# print(c)

# a = 'hello'
# b = len(a)
# print(b)

# def strlength(a):
#     return len(a)


# print(strlength(input('Write Anything: ')))

# P= 123, Area=123
def perimeter_area_rectangle(width, height):
    area = width * height; perimeter = (width+height)*2 ; result = f'P = {perimeter}, Area = {area}' ; return result
print(perimeter_area_rectangle(5,4))