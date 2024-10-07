import turtle as t
import random


monkey = t.Turtle()
monkey.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

monkey.speed("fastest")


def spirograph(size):
    for i in range(int(360/size)):
        monkey.color(random_color())
        monkey.circle(100)
        monkey.setheading(monkey.heading()+10)


spirograph(5)


screen = t.Screen()
screen.exitonclick()





