# assignment 1: Explain what all the functions do
# assignment 2: make a dictionary of 5 things you like and don't like and make a guessing game
# assignment 3: index() and rindex() in lists
# assignment 4: learn keys(), items() and values() in dictionary

# First Assignment Complete in dictionary.py

# Assignment 2:

dict = {
    "ice cream": "like",
    "broccoli": "don't like",
    "hockey": "like",
    "figure skating": "don't like",
    "staying up late": "like",
    "waking up early": "don't like",
    "fruits": "like",
    "vegetables": "don't like",
}
print(dict)

for i in range(3):
    guess = input("Guess what I enjoy! Be careful! You do not have many guesses").lower()


    if dict.get(guess) == "like":
        print("Correct! You know me very well")
        exit()
    if dict.get(guess) == "don't like":
        print("I do not like that thing")
    if i == 2:
        print("You have run out of guesses")
    else:
        print("I do not have an opinion on that thing. Try to guess again!")
print("Try again next time!")
