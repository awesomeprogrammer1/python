from pydoc import text
from tkinter import *
from turtle import fillcolor
root = Tk()
root.title('challenge')
root.resizable(0,0)
canvas=Canvas(root,width=640,height=480)
canvas.pack()
from random import *


class Ball:
    def __init__(self,canvas,paddle,score,color):    
        self.canvas=canvas
        self.id=self.canvas.create_oval(20,20,40,40,fill=color)
        self.canvas.move(self.id,320,240)
        self.paddle=paddle
        self.score=score
        starts=[-4,-5,-3,3,4,5]
        self.x=choice(starts)
        self.y=choice(starts)
        self.hit_bottom = False
    def check_collision(self):
        pos=self.canvas.coords(self.id)
        if pos[0]<=0 or pos[2]>=640:
            self.x=0-self.x
        if pos[1]<=0: 
            self.y=0-self.y
        if pos[3]>=480:
            self.x=0
            self.y=0
            self.score.game_over()
            self.hit_bottom = True
        paddle_pos = self.canvas.coords(self.paddle.id)
        if paddle_pos[0]<=0:
            self.canvas.move(self.paddle.id,0-paddle_pos[0],0)
        if paddle_pos[2]>=640:
            self.canvas.move(self.paddle.id,640-paddle_pos[2],0)
    def hit_paddle(self):
        pos=self.canvas.coords(self.id)
        paddle_pos = self.canvas.coords(self.paddle.id)
        paddle_center = (paddle_pos[0]+paddle_pos[2])/2
        ball_center = (pos[0]+pos[2])/2
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if paddle_pos[1]<=pos[3]<=paddle_pos[3]:
                if ball_center<paddle_center:
                    if self.x>0:
                        self.x=0-self.x
                else:
                    if self.x<0:
                        self.x=0-self.x
                self.canvas.move(self.id,self.x,paddle_pos[1]-pos[3])
                self.y=0-self.y
                self.score.change_score()



    def draw(self):  
        self.canvas.move(self.id,self.x,self.y)
        self.check_collision()
        self.hit_paddle()
class Brick:
    def __init__(self,canvas,ball,score,color,number):
        self.canvas=canvas
        self.score=score
        self.id=canvas.create_rectangle(0+40*number,40,40+40*number,80,fill=color)
        self.ball=ball
        self.exist=True
    def check_collision(self,n):
        if self.exist:
            pos=self.canvas.coords(self.id)
            ball_pos=self.canvas.coords(self.ball.id)
            if (pos[0]<=ball_pos[2]<=pos[2]) or (pos[0]<=ball_pos[0]<=pos[2]):
                if (pos[1]+self.ball.y>=ball_pos[3]>=pos[1]) or (pos[3]+self.ball.y<=ball_pos[1]<=pos[3]):
                    self.ball.y=0-self.ball.y
                    self.canvas.delete(self.id)
                    self.score.change_score(10)
                    self.score.bricks_remaining(n)
                    self.exist=False
            if pos[0]<=ball_pos[2]<=(pos[0]+abs(self.ball.x)) or (pos[2]-abs(self.ball.x)<=ball_pos[0]<=pos[2]):
                if (pos[1]<=ball_pos[3]<=pos[3]) or (pos[1]<=ball_pos[1]<=pos[3]):
                    self.ball.x=0-self.ball.x
                    self.canvas.delete(self.id)
                    self.score.change_score(10)
                    self.score.bricks_remaining(n)
                    self.exist=False
                
class Score:
    def __init__(self,canvas,n,color):
        self.canvas=canvas
        self.score=0
        self.id=canvas.create_text(320,450,text=self.score, font=('Times',16),fill=color)
        self.txt=canvas.create_text(620,460,text='')
        self.n=n
    def bricks_remaining(self,n):
        self.n=n-1
        self.canvas.itemconfig(self.txt,text=self.n)

    def change_score(self,n=1):
        self.score+=n
        self.canvas.itemconfig(self.id,text=self.score)
    def game_over(self):
        self.canvas.move(self.id,0,-220)
        self.canvas.itemconfig(self.id,text='Game Over!')
        

        



class Paddle:
    def __init__(self,canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,120,20, fill=color)
        self.canvas.move(self.id,280,360)
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.speed=5
    def turn_left(self,event):
        self.canvas.move(self.id,0-self.speed,0)
    def turn_right(self,event):
        self.canvas.move(self.id,self.speed,0)

n=4
score = Score(canvas,n, 'black')
paddle = Paddle(canvas, 'teal')
ball=Ball(canvas,paddle,score, 'blue')
wall=[]
for i in range (n):
    brick=Brick(canvas,ball,score,'red',i)
    wall.append(brick)
hit_brick = False

from time import sleep

while not (ball.hit_bottom or hit_brick):
    ball.draw()
    for brick in wall:
        brick.check_collision(len(wall))
        if not brick.exist:
            wall.remove(brick)
    if score.n==0:     
        hit_brick=True  
    root.update_idletasks()
    root.update()
    sleep(0.03)
score.score='Game Over!'
score.canvas.itemconfig(score,text=score.score)        
