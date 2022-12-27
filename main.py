import turtle
from turtle import Turtle, Screen
from random import choice
from extractColor import color_list

turtle.colormode(255)
# below the edited color_list () white color / background color from image.jpg have been removed
# color_list = [(232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253),
#               (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53),
#               (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35),
#               (50, 240, 56)]

screen = Screen()
screen.title("Welcome to the art gallery!")


paint = Turtle()
paint.speed("fastest")


def painting():
    for _ in range(12):
        paint.color(choice(color_list))
        paint.dot(20)
        paint.penup()
        paint.forward(50)
        paint.pendown()


def change_line():
    paint.left(90)
    paint.penup()
    paint.forward(50)
    paint.left(90)
    paint.forward(600)
    paint.setheading(0)


def reset_position():
    # change paintbrush position to left bottom corner
    paint.setheading(225)
    paint.penup()
    paint.forward(400)
    paint.setheading(0)


reset_position()
for _ in range(12):
    painting()
    change_line()

screen.exitonclick()
