import turtle as t




def cube(x=20,y=20,z=20, color='blue'): 
        t.color(color)
        t.forward(x)
        t.left(30)
        t.forward(z)
        t.backward(z)
        t.right(120)
        t.forward(y)
        t.left(120)
        t.forward(z)
        t.backward(z)
        t.right(210)
        t.forward(x)
        t.right(150)
        t.forward(z)
        t.backward(z)
        t.left(60)
        t.forward(y)
        t.right(60)
        t.forward(z)
        t.right(30)
        for i in range (2):
            t.forward(x)
            t.right(90)
            t.forward(y)
            t.right(90)



t.up()
t.goto(-500,-250,)
t.down()
cube(x=50,y=50,z=50,color='yellow')
t.up()
t.goto(0,0)
t.down()
cube(x=250,y=250,z=250,color='green')
input()