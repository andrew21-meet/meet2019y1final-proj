import turtle
import os
def factory():
    os.system("aplay factory.mp3&")


turtle.register_shape("factory.gif")
turtle.penup()
turtle.hideturtle()
turtle.goto(-100, -100)
turtle.showturtle()
turtle.shape("factory.gif")
