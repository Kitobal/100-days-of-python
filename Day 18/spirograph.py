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
timmy.pensize(5)
timmy.speed("fastest")


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()

