from tkinter import messagebox
from easygui import *

# assignment 1
# fix all errors in the calculator


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
        msgbox(added_numbers)
    elif calculator == "subtract":
        subtract_numbers = multenterbox(
            "Write Two Numbers To Subtract from one another",
            "Calculator",
            ["first number", "second number"],
        )
        subtracted_numbers = int(subtract_numbers[0]) - int(subtract_numbers[1])
        msgbox(subtracted_numbers)
    elif calculator == "multiply":
        multiply_numbers = multenterbox(
            "Write Two Numbers To Multiply Together",
            "Calculator",
            ["first number", "second number"],
        )
        multiplied_numbers = int(multiply_numbers[0]) * int(multiply_numbers[1])
        msgbox(multiplied_numbers)
    elif calculator == "divide":
        try:
            divide_numbers = multenterbox(
                "Write Two Numbers To Divide",
                "Calculator",
                ["first number", "second number"],
            )
            divided_numbers = int(divide_numbers[0]) / int(divide_numbers[1])
            msgbox(divided_numbers)
        except ZeroDivisionError:
            msgbox("Error Code 0, DivisionByZero")
        except (TypeError, ValueError):
            msgbox("Error Code 293, Invalid or no input")
    elif calculator == "exponentiate":
        try:
            exponent_numbers = multenterbox(
                "Write two numbers to perform an exponential equation",
                "Calculator",
                ["first number", "second number"],
            )
            exponented_numbers = int(exponent_numbers[0]) ** int(exponent_numbers[1])
            msgbox(exponented_numbers)
        except (ZeroDivisionError):
            msgbox("Error code 293: Exponentiating by zero")
    elif calculator == "exit":
        exit()
