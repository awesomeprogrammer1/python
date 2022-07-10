# intro to dictionaries
# dict[key] = value

dict = {"Hello": "Привет", "Car": "Машина", "Dog": "Собака"}

# get an element
print(
    dict["Hello"]
)  # looks into the dictionary for the specified key and returns the value
print(dict.get("Hello"))  # Returns the value of the specified key
print(
    dict.setdefault("Hello")
)  # Returns the value of the specified key. If the key does not exist then insert the key with the specified value
print(dict)

input()

###################################################

dict = {"Hello": "Привет", "Car": "Машина", "Dog": "Собака"}

# add/remove an element
dict[
    "Cat"
] = "kot"  # adds a new element to the dictionary with the key "cat" and value "kot"
print(dict)

dict.pop(
    "Car"
)  # removes the element with the specified key. If such element does not exist, it returns the last inserted key-value pair
print(dict)

input()

###################################################

dict = {}

# the for statement inserts elements between one and one hundred, which are the keys. Then, the keys are multiplied by two to get the values
for i in range(1, 101):
    dict[i] = i * 2
print(dict)

input()

###################################################

#  all the elements of the list are taken into the dictionary, which are the keys. The keys are then divided by two, thus giving us the values
list = [1, 2, 5, 473, 987, 560, 35]
dict = {}
for i in list:
    dict[i] = i / 2

# all the elements of the list that are even are put into the dictionary as keys and then multiplied by two for the values
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
