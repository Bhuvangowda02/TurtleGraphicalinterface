from turtle import Turtle, Screen
import random


monkey = Turtle()
monkey.shape("turtle")
monkey.color("cyan1")

colours =  ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def shape(sides):
    angle = 360 / sides
    for i in range(sides):
        monkey.forward(100)
        monkey.right(angle)

for shapes in range(3,11):
    monkey.color(random.choice(colours))
    shape(shapes)


















screen = Screen()
screen.exitonclick()
