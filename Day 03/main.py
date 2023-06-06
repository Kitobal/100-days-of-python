print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇


choice1 = input("You encounter a bifurcated path, you can go right or left. type R or L.").lower()
if choice1 == "r":
    print("You fell into a hole and died")
    print("GAME OVER")
elif choice1 == "l":
    print("You chose the left path and found a room with 3 doors. a Red one, a Black one, and  Blue one.")
    choice2 = input("type Red, Black or Blue ").lower()
    if choice2 == "red":
        print("You walk into a trap an die")
        print("GAME OVER")
    elif choice2 == "Blue":
        print("You encounter a little lake")
        choice3 = input("Swim trough the lake or go around, type S for swim or A for going around").lower
        if choice3 == "s":
            print("you are making your way across and you get eaten by a monster")
            print("GAME OVER")
        else:
            print("You found the tressure")
            print("YOU WIN")
    else:
        print("You found a dead end and died of boredom.")
        print("GAME OVER")
else:
    print("you took to long to choose and a giant rock fell on your head, killing you.")
    print("GAME OVER")