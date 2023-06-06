import random
paper = "✋"
scissors = "✌️"
rock = "✊"
options = [rock,paper,scissors]
choice = input("Rock, Paper or Scissors? type R or P or S ")
comchoice = options[random.randint(0,2)]
if choice == "R":
    if comchoice == "✊":
        print(f"you: {rock} vs com: {rock}")
        print("Tie")
    elif comchoice == "✌️":
        print(f"you: {rock} vs com: {scissors}")
        print("You Win")
    elif comchoice == "✋":
        print(f"you: {rock} vs com: {paper}")
        print("You Lose")
elif choice == "P":
    if comchoice == "✊":
        print(f"you: {paper} vs com: {rock}")
        print("You Win")
    elif comchoice == "✌️":
        print(f"you: {paper} vs com: {scissors}")
        print("You Lose")
    elif comchoice == "✋":
        print(f"you: {paper} vs com: {paper}")
        print("Tie")
elif choice == "S":
    if comchoice == "✊":
        print(f"you: {scissors} vs com: {rock}")
        print("You Lose")
    elif comchoice == "✌️":
        print(f"you: {scissors} vs com: {scissors}")
        print("Tie")
    elif comchoice == "✋":
        print(f"you: {scissors} vs com: {paper}")
        print("You Win")
else:
    print("Invalid input")