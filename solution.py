import turtle as t
from turtle import Screen
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim = t.Turtle()
    # angle = 360 / num_sides
    # for _ in range(num_sides):
        # tim.forward(100)
        # tim.right(angle)


# for shape_side_n in range(3, 11):
    # tim.color(random.choice(colors))
    # draw_shape(shape_side_n)

# Challenge 5: Random Walk; My try: solution: (didn't need the function)
tim.shape("turtle")
tim.color("aquamarine")
tim.speed(9)
tim.pensize(10)
directions = [0, 90, 180, 270]

def random_walk():
    for _ in range(200):
        tim.setheading(random.choice(directions))
        tim.forward(30)
        tim.color(random_color())


random_walk()

screen = Screen()
screen.exitonclick()
