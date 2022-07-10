# assignment 1: Explain what all the functions do
# assignment 2: make a dictionary of 5 things you like and don't like and make a guessing game
# assignment 3: index() and rindex() in lists
# assignment 4: learn keys(), items() and values() in dictionary

# First Assignment Complete in dictionary.py

# Assignment 2:

dict = {
    "ice cream": "Like",
    "broccoli": "don't like",
    "hockey": "Like",
    "figure skating": "don't like",
    "staying up late": "Like",
    "waking up early": "don't like",
    "fruits": "Like",
    "vegetables": "don't like",
}
print(dict)

for i in range(3):
    guess = input("Guess what I enjoy! Be careful! You do not have many guesses: ")
    if dict.get(guess) == "Like":
        print("Correct! You Know Me Very Well")
        exit()
    if dict.get(guess) == "don't like":
        print("I do not like that thing")
    else:
        print("I do not have an opinion on that thing. Check for a typo and make sure that all letters are lowercase. Otherwise, try again!")
print("You ran out of guesses. Try again!")
