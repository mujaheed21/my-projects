__author__ = 'Feedah'
import turtle
def Draw_square():
    window = turtle.Screen()
    window.bgcolor("light blue")
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(1)
    nombr = 0
    while nombr<4:
        brad.left(90)
        brad.forward(100)
        brad.left(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        nombr=nombr + 1
    window.exitonclick()
Draw_square()

