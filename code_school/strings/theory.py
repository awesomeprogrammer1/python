string_var = "Hello, World!"

# method index return
# returns the index of "e" (where it is first found)
# print(string_var.index("e")) #  1


# method lower
# converts the entire string to lowercase
# print(string_var.lower()) # hello, world!


# method upper
# print(string_var.upper()) # HELLO, WORLD!
# converts the whole string to upper case

# method split
# seperates the string by the character given by the user
# print(string_var.split(",") # ["Hello", "World!"]


# method strip
# creates a copy of the string without a certain character(s)
# print(string_var.strip("H") # ello, World!


# method replace
# returns a copy of the string in which a certain character(s)

# print(string_var.replace("H", "J")) # Jello, World!


# method capitolize
# makes the first letter capitolized, and the rest lowercase
# print(string_var.capitalize()) # Hello, world!


# method casefold
# basically just another version of lower(), but more strict
# print(string_var.casefold()) # hello, world!

# method rindex
# finds how far the given character
# (if there are duplicates, it takes the first one)
# is from the end of the string
# print(string_var.rindex("l")) # 10

# method swapcase
# self explainitory: converts upper case to lower case and vice versa
# print(string_var.swapcase()) # hELLO, wORLD!


# method format
# Makes the first letter in each word upper case
# print(string_var.format()) # Hello, World!


# method partition
# seperates the string into parts by a given
# character
# print(string_var.partition("l")) # ('He', 'l', 'lo, World!')

# function len
# returns the amount of items in the string or list in question
# print(len(string_var)) # 13

# method isupper, islower, and istitle
# all of these methods return True/False (bool)
# for istitle, we can normally print it out
# string_var_txt = string_var.istitle()
# print(string_var_txt) # True
# for isupper and islower, we can use a for loop
# to better demonstrate the capabilities

for element in string_var:
    element_upper = element.isupper()
    element_lower = element.islower()
    if element_upper is True:
        print("Letter is upper case")
    if element_lower is True:
        print("Letter is lower case")

# method join
# takes all items in an iterable and joins them into one string
# a string must be specified as the seperator
# Tuple_Var = ("Andrew", "Sergei", "Sasha")
# a = "!".join(Tuple_Var)
# print(a)
# Result: Andrew!Sergei!Sasha
