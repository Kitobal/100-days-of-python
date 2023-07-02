import random
import tkinter
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pwd():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    pwd_input.delete(0, tkinter.END)
    pwd_input.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user = user_input.get()
    password = pwd_input.get()
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \nUser: {user}\n"
                                                      f"Password: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                website_input.delete(0, tkinter.END)
                # user_input.delete(0, tkinter.END)
                pwd_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website label
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

# website entry
website_input = tkinter.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# user label
user_label = tkinter.Label(text="Username/Email:")
user_label.grid(row=2, column=0)

# user entry
user_input = tkinter.Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "example@email.com")

# pwd label
pwd_label = tkinter.Label(text="Password:")
pwd_label.grid(row=3, column=0)

# pwd entry
pwd_input = tkinter.Entry(width=20)
pwd_input.grid(row=3, column=1)

# pwd button
pwd_button = tkinter.Button(text="Generate Password", command=generate_pwd)
pwd_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
