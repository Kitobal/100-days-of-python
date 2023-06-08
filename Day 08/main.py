from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keepRunning = True

def Caesar(inputText,inputShift,inputDir):
    outputText = ""
    if inputDir == "decode":
        inputShift *= -1
    for letter in inputText:
        if letter in alphabet:
            index = alphabet.index(letter)
            newindex = index + inputShift
            outputText += alphabet[newindex]
        else:
            outputText += letter
    print(f"{inputDir}d text: {outputText}")  

print(logo)  
while keepRunning:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    Caesar(text,shift,direction)
    again = input("Type 'yes' if you want to go again. otherwise type 'no'\n")
    if again == "no":
        keepRunning = False
        print("Goodbye")

