#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

randomletters = ""
for i in range(1,nr_letters +1):
    randomletters = randomletters + random.choice(letters)
randomsymbols = ""
for i in range(1,nr_symbols +1):
    randomsymbols = randomsymbols + random.choice(symbols)
randomnumbers = ""
for i in range(1,nr_numbers +1):
    randomnumbers = randomnumbers + random.choice(numbers)
easypwd = randomletters + randomsymbols + randomnumbers
#print(f"Your password : {easypwd}")

#Hard Level - Order of characters randomised:

pwdlist = list(easypwd) #convert the string to a list
random.shuffle(pwdlist) #shuffles the list
hardpwd = "".join(pwdlist) #converts the list to string
print(f"Your password : {hardpwd}")