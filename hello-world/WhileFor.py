name = input('Hello! What is your name?')
for i in range(5):
    age = int(input('How old are you?'))
    if age == 12:
        print('Correct again', name)
        break
    else:
        print('Wrong. Try again!')