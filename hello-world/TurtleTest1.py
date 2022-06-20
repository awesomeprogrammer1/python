import turtle as t

t.speed = 1
i= int(input('How many sides will your shape have? '))
counter = 1
while i>=counter:
    t.forward(100)
    t.right(360/i)
    counter+=1
    print(i)
    