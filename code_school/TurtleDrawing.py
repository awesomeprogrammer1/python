import turtle as t

LENGTH = 120
WIDTH = LENGTH * 2 / 3


def draw_one(x, y):
    t.penup()
    t.goto(x + WIDTH, y + 0)
    t.pendown()
    t.goto(x + WIDTH, y - LENGTH)
    t.penup()


def draw_two(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + WIDTH, y + 0)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + 0, y - LENGTH)
    t.goto(x + WIDTH, y - LENGTH)
    t.penup()


def draw_three(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + WIDTH, y + 0)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + 0, y - LENGTH)
    t.penup()


def draw_four(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + WIDTH, y + 0)
    t.goto(x + WIDTH, y - LENGTH)
    t.penup()


def draw_five(x, y):
    t.penup()
    t.goto(x + WIDTH, y + 0)
    t.pendown()
    t.goto(x + 0, y + 0)
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + 0, y - LENGTH)
    t.penup()


def draw_six(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 0, y - LENGTH)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + 0, y - LENGTH / 2)
    t.penup()


def draw_seven(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + WIDTH, y + 0)
    t.goto(x + WIDTH, y - LENGTH)
    t.penup()


def draw_eight(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 0, y - LENGTH)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + WIDTH, y + 0)
    t.goto(x, y)
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.penup()


def draw_nine(x, y):
    t.penup()
    t.goto(x + WIDTH, y + 0)
    t.pendown()
    t.goto(x, y)
    t.goto(x + 0, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH / 2)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + WIDTH, y + 0)
    t.penup()


def draw_zero(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 0, y - LENGTH)
    t.goto(x + WIDTH, y - LENGTH)
    t.goto(x + WIDTH, y + 0)
    t.goto(x, y)
    t.penup()


def draw_number(s):
    digets = []
    while s > 0:
        digets.append(s % 10)
        s = s // 10
    start = (0 - len(digets) // 2) * WIDTH
    digets.reverse()
    for i in digets:
        if i == 1:
            draw_one(start, 0)
        if i == 2:
            draw_two(start, 0)
        if i == 3:
            draw_three(start, 0)
        if i == 4:
            draw_four(start, 0)
        if i == 5:
            draw_five(start, 0)
        if i == 6:
            draw_six(start, 0)
        if i == 7:
            draw_seven(start, 0)
        if i == 8:
            draw_eight(start, 0)
        if i == 9:
            draw_nine(start, 0)
        if i == 0:
            draw_zero(start, 0)
        start = start + WIDTH + WIDTH / 6
    input()


def main():
    s = int(input("What number will you choose to draw out? "))
    draw_number(s)


main()
