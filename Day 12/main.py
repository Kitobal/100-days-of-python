import random
from art import logo

print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1,100)
attempts = 0
difficulty = input("Choose a dificulty, type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5
print(f"You have {attempts} attempts remaining.")
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"Correct the number was {number}")
        attempts = 0
    elif guess > number:
        print("Too High, guess again")
        attempts -= 1
        if attempts == 0:
            print(f"You ran out of attempts, the number was {number}")
        else:
            print(f"You have {attempts} attempts remaining.")
    else:
        print("Too Low, guess again")
        attempts -= 1
        if attempts == 0:
            print(f"You ran out of attempts, the number was {number}")
        else:
            print(f"You have {attempts} attempts remaining.")