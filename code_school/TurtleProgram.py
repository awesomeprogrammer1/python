colors = ['red', 'orange','yellow','green','blue','purple','pink','light blue','black','teal']
import random 
import turtle as t
t.speed(0)
i= int(input('How many sides will your shape have? '))
x,y= input('Where will the shape start? (at what coordinates) ').split()
x=int(x)
y=int(y)
while i !=2:
    t.penup()
    t.goto(x,y)
    t.pendown()
    random.shuffle(colors)
    t.color(colors[0])
    counter = 1
    t.begin_fill()
    while i>=counter:
        t.forward(30)
        t.right(360/i)
        counter+=1
        print(i)
    i-=1
    t.end_fill()
    x+=30