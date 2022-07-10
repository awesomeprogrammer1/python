# assignment 1: Explain what all the functions do
# assignment 2: make a dictionary of 5 things you like and don't like and make a guessing game
# assignment 3: index() and rindex() in lists
# assignment 4: learn keys(), items() and values() in dictionary

# First Assignment Complete in dictionary.py


# Assignment 2:


dict = {
    "Ice Cream": "Broccoli",
    "Hockey": "Figure Skating",
    "Being with friends": "Sitting at home",
    "Staying up Late": "Waking up early",
    "Fruits": "Vegetables",
}
print(dict)
thisdict = dict.fromkeys(dict, "Like")
thatdict = dict.values()

guess = input("Guess what I enjoy! ")


if guess in thisdict:
    print("Correct! You Know Me Very Well")
    exit()
else:
    print("I either do not like that thing, or I do not have an opinion on it. Try to be more specific next time!")
if guess in thatdict:
    print("I do not like that thing")
    exit()
else:
    print("I do not have an opinion on that. Try to be more specific! ")
    exit()
