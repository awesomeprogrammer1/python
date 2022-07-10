dict = {
   "Hello": "Привет",
    "Car": "Машина",
    "Dog": "Собака"
}

print(dict["Hello"]) #
print(dict.get("Hello")) #
print(dict.setdefault("Hello")) #
print(dict)

input()

###################################################

dict = {
   "Hello": "Привет",
    "Car": "Машина",
    "Dog": "Собака"
}

dict["Cat"] = "kot" # dict[key] = value
print(dict)

dict.pop("Car") #
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
