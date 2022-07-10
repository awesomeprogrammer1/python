# intro to dictionaries
# dict[key] = value

dict = {
   "Hello": "Привет",
    "Car": "Машина",
    "Dog": "Собака"
}

# get an element
print(dict["Hello"]) # get element from list and print
print(dict.get("Hello")) # returns the value for the key if the key is in the dictionary, if it isnt, print default
print(dict.setdefault("Hello")) # sets hello as the default element
print(dict)

input()

###################################################

dict = {
   "Hello": "Привет",
    "Car": "Машина",
    "Dog": "Собака"
}


# add/remove an element
dict["Cat"] = "kot" # adds a new element to the dictionary
print(dict)

dict.pop("Car") # removes a current existing element
print(dict)

input()

###################################################

dict = {}

for i in range(1, 101):
    dict[i] = i * 2
print(dict)

input()

###################################################

list = [1, 2, 5, 473, 987, 560, 35]
dict = {}
for i in list:
    dict[i] = i/2

for i in list:
    if i % 2 == 0:
        dict[i] = i * 2
print(dict)

input()

###################################################

dict = {}

user_string = input("Enter a string: ")

for letter in user_string:
    if not letter in dict.keys():
        dict[letter] = user_string.count(letter)
print(dict)
