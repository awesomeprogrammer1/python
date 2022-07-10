# dict = {
#    "Hello": "Привет",
#     "Car": "Машина",
#     "Dog": "Собака"
# }

# assignment 1: Explain what all the functions do
# assignment 2: make a dictionary of 5 things you like and don't like and make a guessing game
# assignment 3: index and rindex in lists 
# assignment 4: learn keys items and values in dictionary




# print(dict["Hello"]) #
# print(dict.get("Hello")) #
# print(dict.setdefault("Hello")) #
# print(dict)


# dict["Cat"] = "kot" # dict[key] = value
# print(dict)

# dict.pop("Car") #
# print(dict)

# dict = {}

# for i in range(1, 101):
#     dict[i] = i * 2
# print(dict)


# list = [1, 2, 5, 473, 987, 560, 35]
# dict = {}
# for i in list:
#     dict[i] = i/2

# for i in list:
#     if i % 2 == 0:
#         dict[i] = i * 2
# print(dict)

dict = {}

user_string = input("Enter a string: ")

for letter in user_string:
    if not letter in dict.keys():
        dict[letter] = user_string.count(letter)
print(dict)
