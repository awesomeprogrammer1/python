# In python everything is an object
"""
In Python, self is a conventional name used as the first parameter 
in the definition of a method within a class.
It represents the instance of the class on which the method is being called.

When you define a method in a class, you need to include the self parameter as the first parameter, 
even though you don't explicitly pass an argument for it when calling the method.
Python automatically handles this for you behind the scenes.

Explaination:
Imagine you have a bunch of different toys, each with its own special features and abilities. 
Now, let's say you want to organize these toys and make them interact with each other. 
That's where object-oriented programming (OOP) comes in!


In OOP, we think of our program as a big collection of objects, just like your toys. 
Each object is like a mini-program that has its own set of characteristics (called properties) and things it can do (called methods).
Think of a toy car, for example. It has properties like its color, size, and number of wheels. 
It can also do things like move forward, turn, and honk its horn. These properties and methods define what the toy car is and what it can do.
Now, in OOP, we can create many toy cars based on a blueprint called a "class." 
A class is like a template that describes the properties and methods that each toy car should have. It's like a set of instructions for building the car.
When we create a toy car from the class, we call it an "object" or an "instance" of the class. 
It's like making a real toy car using the blueprint. 
Each object is independent and can have its own unique values for the properties. 
For example, one toy car can be red, while another can be blue.
The cool thing about OOP is that objects can interact with each other. 
Let's say you have a toy car and a toy garage. 
You can write code that allows the car to drive into the garage. 
The car and the garage are both objects, and you can make them work together by using their methods.


"""

str_var = "hello world"


class Tiger:
    def __init__(self, name):
        self.name = name

    def growl(self):
        return f"Tiger {self.name}: rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"


tiger_andrew = Tiger("Andrew")
tiger_sergei = Tiger("Sergei")

print(type(tiger_andrew), type(tiger_sergei), type(str_var))
print(tiger_andrew.growl())
print(tiger_sergei.growl())
print(str_var.upper())
