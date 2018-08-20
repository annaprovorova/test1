#простейшие фракталы
from turtle import Turtle

#кривая Коха
def koch_forward(L, n):
    if n == 0:
        t.forward(L)
    else:
        koch_forward(L/3, n-1)
        t.left(60)
        koch_forward(L/3, n-1)
        t.right(120)
        koch_forward(L/3, n-1)
        t.left(60)
        koch_forward(L/3, n-1)

#снежинка Коха
def snowflake():
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.color('black', 'cyan')
    t.begin_fill()
    for edge in range(3):
        koch_forward(300, 4)
        t.right(120)
    t.end_fill()

def demo():
    for n in range(0, 4):
        t.color(colors[n])
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        koch_forward(300, n)

def snowflake():
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.color('black', 'cyan')
    t.begin_fill()
    for edge in range(3):
        koch_forward(300, 4)
        t.right(120)
    t.end_fill()

t = Turtle(shape='turtle')
colors = ['gray', 'magenta', 'blue', 'cyan']
t.speed(10)
snowflake()
t.hideturtle()
