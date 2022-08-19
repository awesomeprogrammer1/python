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
# removes a certain letter from the string
# print(string_var.strip("H") # ello, World!


# method replace
# exchanges one letter already in the string for another letter
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
