__author__ = 'Feedah'
import turtle

def Draw_square():
    window = turtle.Screen()
    window.bgcolor("light blue")
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(1)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    angie = turtle.Turtle()
    angie.circle(50)
    window.exitonclick()
Draw_square()
