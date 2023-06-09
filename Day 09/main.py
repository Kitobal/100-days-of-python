# from replit import clear
from art import logo

moreBidders = True
bids = {}
print(logo)

while moreBidders:
  name = input("What is your name? ")
  amount =  int(input("What's your bid? $"))
  bids[name] = amount
  answer = input("Are there any other bidders? Type 'yes' or 'no' ")
  if answer == "no":
    moreBidders = False
#   else:
#     clear()

highest = 0

for bidder in bids:
  if bids[bidder] > highest:
    highest = bids[bidder]
    winner = bidder

print(f"The winner is {winner} with a bid of ${highest}")