# assignment 1: Explain what all the functions do
# assignment 2: make a dictionary of 5 things you like and don't like and make a guessing game
# assignment 3: index() and rindex() in lists
# assignment 4: learn keys(), items() and values() in dictionary

# First Assignment Complete in dictionary.py


# Assignment 2:




dict = {
    "Ice Cream": "Like",
    "broccoli": "don't like",
    "hockey": "Like",
    "figure skating": "don't like",
    "staying up late": "Like",
    "waking up early": "don't like",
    "fruits" : "Like",
    "vegetables" : "don't like"

}
print(dict)
# thisdict = dict.fromkeys(dict, "Like")
# thatdict = dict.fromkeys(dict, "don't like")

testdict = dict.values()
print(testdict)

guess = input("Guess what I enjoy! ")


if dict.setdefault(guess) == "Like":
    print("Correct! You Know Me Very Well")
    exit()
if dict.setdefault(guess) == "don't like":
    print("I do not like that thing")
    exit()
else:
    print('I do not have an opinion on that thing, or you may have had a typo. Try again, there may be a problem with capital letters at the start')

