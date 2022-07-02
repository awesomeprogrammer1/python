name = input("Hello! What is your name? ")
for i in range(5):
    age = int(input("How old are you? "))
    if age == 12:
        print("Correct again", name)
        break
    else:
        if i < 4:
            print("Wrong. Try again!")
        else:
            print("You are out of guesses, better luck next time!")
