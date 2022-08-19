string_var = "Hello, World!"

# method index return
# print(string_var.index("e")) #  1
# returns the index of "e" (where it is first found)

# method lower
# print(string_var.lower()) # hello, world!
# converts the entire string to lowercase

# method upper
# print(string_var.upper()) # HELLO, WORLD!
# converts the whole string to upper case

# method split
# print(string_var.split(",") # ["Hello", "World!"]
# seperates the string by the character given by the user

# method strip
# print(string_var.strip("H") # ello, World!
# removes a certain letter from the string

# method replace
# print(string_var.replace("H", "J")) # Jello, World!
# exchanges one letter already in the string for another letter

# method capitolize
# print(string_var.capitalize()) # Hello, world!
# makes the first letter capitolized, and the rest lowercase

# method casefold
# print(string_var.casefold()) # hello, world!
# basically just another version of lower()

# method rindex
# print(string_var.rindex("l")) # 10
# finds how far the given character
# (if there are duplicates, it takes the first one)
# is from the end of the string

# method swapcase
# print(string_var.swapcase()) # hELLO, wORLD!
# self explainitory: converts upper case to lower case and vice versa

# method format
# print(string_var.format()) # Hello, World!
# Makes the first letter in each word upper case

# method partition
# print(string_var.partition("l")) # ('He', 'l', 'lo, World!')
# seperates the string into parts by a given
# character
