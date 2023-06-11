import random
from art import logo

cards = {
    "A":11, 
    "2":2,
    "3":3, 
    "4":4, 
    "5":5, 
    "6":6, 
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10}
symbols = ["♠","♣","♥","♦"]
def dealCard():
    randomCard = random.choice(list(cards.keys()))
    return [randomCard,cards[randomCard],random.choice(symbols)]

def calculateScore(cardlist):
    score = 0
    for card in cardlist:
        score += card[1]
    if len(cardlist) == 2 and score == 21:
        return 0 #blackjack!
    if any("A" in sublist for sublist in cardlist) and score > 21:
        score = score - 10
    return score

def displayUserCards(cardlist):
    display = "Your cards: "
    for card in cardlist:
        display += "|"+ card[0]+" "+ card[2]+"|"
    return display

def displayDealerStarter(cardlist):
    display = "Dealer cards: "
    display += "|"+ cardlist[0][0]+" "+ cardlist[0][2]+"||░░░|"
    return display

def displayDealerCards(cardlist):
    display = "Dealer cards: "
    for card in cardlist:
        display += "|"+ card[0]+" "+ card[2]+"|"
    return display

def compare(uscore,comscore):
    if uscore == comscore:
        return "DRAW"
    elif comscore == 0:
        return "Dealer Blackjack, YOU LOSE"
    elif uscore == 0:
        return "Blackjack! YOU WIN"
    elif uscore > 21:
        return "You Bust, YOU LOSE"
    elif comscore > 21:
        return "Dealer Bust, YOU WIN"
    elif uscore > comscore:
        return "YOU WIN"
    else:
        return "YOU LOSE"
    
def playGame():
    print(logo)
    userCards = []
    computerCards = []
    gameOver = False
    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not gameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print("\n"+displayDealerStarter(computerCards))
        print(displayUserCards(userCards)+f" Score: {userScore}")
        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            userHit = input("\nType h' to Hit(get another card) or 's' to Stand: ")
            if userHit == "h":
                userCards.append(dealCard())
            else:
                gameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)
    print("\n"+displayDealerCards(computerCards)+f" Score: {computerScore}")
    print(displayUserCards(userCards)+f" Score: {userScore}")
    print(compare(userScore,computerScore)+"\n")


while input("Play a hand of Blackjack? Type 'y' or 'n': ") == "y":
    playGame()