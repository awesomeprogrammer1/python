from easygui import *

# assignment 1
# And add an exponent operation
# Also handle division by zero


while True:
    calculator = buttonbox(
        "Choose to add, subtract, multiply, or divide",
        "Calculator",
        ["add", "subtract", "multiply", "divide", "exponentiate", "exit"],
    )
    if calculator == "add":
        add_numbers = multenterbox(
            "Write Two Numbers To Add Together",
            "Calculator",
            ["first number", "second number"],
        )
        added_numbers = int(add_numbers[0]) + int(add_numbers[1])
        textbox(added_numbers)
    elif calculator == "subtract":
        subtract_numbers = multenterbox(
            "Write Two Numbers To Subtract from one another",
            "Calculator",
            ["first number", "second number"],
        )
        subtracted_numbers = int(subtract_numbers[0]) - int(subtract_numbers[1])
        textbox(subtracted_numbers)
    elif calculator == "multiply":
        multiply_numbers = multenterbox(
            "Write Two Numbers To Multiply Together",
            "Calculator",
            ["first number", "second number"],
        )
        multiplied_numbers = int(multiply_numbers[0]) * int(multiply_numbers[1])
        textbox(multiplied_numbers)
    elif calculator == "divide":
        divide_numbers = multenterbox(
            "Write Two Numbers To Divide",
            "Calculator",
            ["first number", "second number"],
        )
        if divide_numbers[0] or divide_numbers[1] == 0:
            textbox("Error code 000: One or more numbers equivilant to zero")
        else:
            divided_numbers = int(divide_numbers[0]) / int(divide_numbers[1])
            textbox(divided_numbers)
    elif calculator == "exponentiate":
        exponent_numbers = multenterbox(
            "Write two numbers to perform an exponential equation",
            "Calculator",
            ["first number", "second number"],
        )
        if exponent_numbers[0] or exponent_numbers[1] == 0:
            textbox("Error code 000: One or more numbers equivilant to zero")
        else:
            exponented_numbers = int(exponent_numbers[0]) ^ int(exponent_numbers[1])
            textbox(exponented_numbers)
    elif calculator == "exit":
        exit()
