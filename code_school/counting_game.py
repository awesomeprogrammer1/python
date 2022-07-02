from os import kill
from random import random
from tkinter import END


number = random.randint(1,100)
number_of_guesses = 0

guess_the_number = int(input('Guess a number between 1 and 100 '))
if guess_the_number == number:
    print('That was the correct number! Good job!')
    
while guess_the_number != number:
    print('Incorrect, try again ')
    number_of_guesses+1

if number_of_guesses >= 5:
    print('Your out of guesses!Try again')
   