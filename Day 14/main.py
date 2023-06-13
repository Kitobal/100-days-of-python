import random
from art import logo,versus
from game_data import data

def HasMoreFollowers(account1,account2):
    if account1['follower_count'] > account2['follower_count']:
        return True
    else:
        return False

score = 0
gameOver = False
print(logo)

accountA = random.choice(data)
while not gameOver:
    accountB = random.choice(data)
    while accountA == accountB:
        accountB = random.choice(data)

    print(f"\nCompare A: {accountA['name']}, {accountA['description']}, from {accountA['country']}")
    print(versus)
    print(f"Compare B: {accountB['name']}, {accountB['description']}, from {accountB['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == "a" or choice == "A":
        if HasMoreFollowers(accountA,accountB):
            print(f"Correct, Current score: {score}")
            score += 1
            accountA = accountB
        else:
            print("Wrong, GAME OVER")
            print(f"Your score: {score}")
            gameOver = True
    else:
        if HasMoreFollowers(accountB,accountA):
            print(f"Correct, Current score: {score}")
            score += 1
            accountA = accountB
        else:
            print("Wrong, GAME OVER")
            print(f"Your score: {score}")
            gameOver = True
