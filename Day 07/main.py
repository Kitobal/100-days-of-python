import random
import asciiart
import words
lives = 6
chosen_word = random.choice(words.word_list)
#print(f"the solution is {chosen_word}") # for testing
display = []
for letter in chosen_word:
    display.append("_")
game_over = False
print(asciiart.title)
print(f"{' '.join(display)}")
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")
    for position in range(len(chosen_word)):
        if chosen_word[position]== guess:
            display[position]= guess
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong, {guess} is not part of the word")
        if lives < 1:
            game_over = True
            print("You Lose")
            print(f"The word was: {chosen_word}")
    else:
        print("Correct")
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_over = True
        print("You Win")
    print(asciiart.stages[lives])

