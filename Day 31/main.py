import random
import tkinter
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---import data from csv--- #
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("data/french_words.csv")
    to_learn = data_frame.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")


# ---Functions--- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_card["French"], fill="black")
    card.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")
    card.itemconfig(card_bg, image=card_back)


def is_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ---UI Setup--- #

window = tkinter.Tk()
window.title("French Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# Card
card = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
card_bg = card.create_image(400, 263, image=card_front)
card_title = card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = card.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

correct_image = tkinter.PhotoImage(file="images/right.png")
correct_button = tkinter.Button(image=correct_image, highlightthickness=0, borderwidth=0, command=is_known)
correct_button.grid(row=1, column=1)


next_card()
window.mainloop()
