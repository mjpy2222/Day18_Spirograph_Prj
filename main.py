# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# tim.shape("turtle")
# tim.color("aquamarine")

# for _ in range(4):
# tim.forward(100)
# tim.right(90)

from turtle import Turtle, pendown, penup,  Screen

tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine")

# for _ in range(15):
# tim.forward(10)
# tim.penup()
# tim.forward(10)
# tim.pendown()


def triangle():
    tim.pencolor("deep pink")
    for _ in range(3):
        tim.forward(100)
        tim.right(120)


def square():
    tim.pencolor("yellow")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def pentagon():
    tim.pencolor("orange")
    for _ in range(5):
        tim.forward(100)
        tim.right(72)


def hexagon():
    tim.pencolor("light green")
    for _ in range(6):
        tim.forward(100)
        tim.right(60)


def heptagon():
    tim.pencolor("purple")
    for _ in range(7):
        tim.forward(100)
        tim.right(51.5)


def octagon():
    tim.pencolor("cyan")
    for _ in range(8):
        tim.forward(100)
        tim.right(45)


def nonagon():
    tim.pencolor("blue")
    for _ in range(9):
        tim.forward(100)
        tim.right(40)


def decagon():
    tim.pencolor("sea green")
    for _ in range(10):
        tim.forward(100)
        tim.right(36)


# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()























screen = Screen()
screen.exitonclick()

