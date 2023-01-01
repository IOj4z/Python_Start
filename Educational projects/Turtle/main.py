import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size, angle, shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)


turtle.speed('fast')
turtle.pensize(4)
draw_circle(30, 0, 1)

# import turtle as t
#
#
#
# def rectangle(horizontal, vertical, color):
#     t.pendown()
#     t.pensize()
#     t.color(color)
#     t.begin_fill()
#     for counter in range(1, 3):
#         t.forward(horizontal)
#         t.right(90)
#         t.forward(vertical)
#         t.right(90)
#     t.end_fill()
#     t.penup()
#     t.speed('slow')
#     t.bgcolor('Dodger blue')
