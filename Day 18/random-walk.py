import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")

direction = [0, 90, 180, 270]

for _ in range(100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = t.Screen()
screen.exitonclick()

