import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Wich turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won, {winner} is the winner!")
            else:
                print(f"You lose, {winner} was the winner.")
        amount = random.randint(0, 10)
        turtle.forward(amount)


screen.exitonclick()
