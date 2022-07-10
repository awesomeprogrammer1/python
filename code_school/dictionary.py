# intro to dictionaries
# dict[key] = value

 
print(dict)
dict = {"Hello": "Привет", "Car": "Машина", "Dog": "Собака"}

# returns the value if the key exists. If it doesn't, there is an error
print(dict["Hello"])
# returns the value if the key exists. If it doesn't, the method returns "None"
print(dict.get("Hello"))  
# returns the value and adds the key to the dictionary if it exists. If it doesnt, it returns "None" and adds the key to the list with value "None"
print(dict.setdefault("Hello"))
input()

###################################################

dict = {"Hello": "Привет", "Car": "Машина", "Dog": "Собака"}

# add/remove an element


# adds a new element to the dictionary with the key "cat" and value "kot"
dict["Cat"] = "kot"
print(dict)


# Removes the specified key from the dictionary. If the key does not exist, there is an error
dict.pop("Car")
print(dict)

input()

###################################################

dict = {}

# Add 100 elements to the dictionary
# with all keys being a number from 1-100.
# The value of the element is the key multiplied by two
for i in range(1, 101):
    dict[i] = i * 2
print(dict)

input()

###################################################

# We are adding things to the dictionary.
# We add the elements into the dictionary.
# We get the value of the element by dividing the key, which is the number in the list, by two.
list = [1, 2, 5, 473, 987, 560, 35]
dict = {}
for i in list:
    dict[i] = i / 2

# all the elements are put into the dictionary. Then, all the keys that are even are multiplied by two
# in order to obtain the value of the element
for i in list:
    if i % 2 == 0:
        dict[i] = i * 2
print(dict)

input()

####################################################


# we create an new empty dictionary
# we prompt the user for a string
# we fill the dictionary with the letters that were in the string
# if there is a character that appears more than once (ex. 6 times)
# we don't add it again, but we add it to the total amount of identical characters there are in the string
# ex: 'a' = 6
dict = {} 

user_string = input("Enter a string: ")

for letter in user_string:
    if not letter in dict.keys():
        dict[letter] = user_string.count(letter)
print(dict)
