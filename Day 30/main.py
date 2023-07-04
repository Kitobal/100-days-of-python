import random
import json
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
    new_data = {
        website: {
            "user": user,
            "password": password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read-update in json file
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            # if data.json file does not exist:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # write in json
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            # user_input.delete(0, tkinter.END)
            pwd_input.delete(0, tkinter.END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showwarning(title="Empty field", message="Website field is empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read-update in json file
                data = json.load(data_file)
        except FileNotFoundError:
            # if data.json file does not exist:
            messagebox.showerror(title="File not Found", message="No data file found.")
        else:
            try:
                website_data = data[website]
            except KeyError:
                messagebox.showwarning(title="Website not Found", message=f"No data found for {website}")
            else:
                messagebox.showinfo(title=website, message=f"User/Email: {website_data['user']}\n"
                                                           f"Password: {website_data['password']}")


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
website_input = tkinter.Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()

# website search button
website_button = tkinter.Button(text="Search",command=search, width=16)
website_button.grid(row=1, column=2)

# user label
user_label = tkinter.Label(text="Username/Email:")
user_label.grid(row=2, column=0)

# user entry
user_input = tkinter.Entry(width=52)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "example@email.com")

# pwd label
pwd_label = tkinter.Label(text="Password:")
pwd_label.grid(row=3, column=0)

# pwd entry
pwd_input = tkinter.Entry(width=32)
pwd_input.grid(row=3, column=1)

# pwd button
pwd_button = tkinter.Button(text="Generate Password", command=generate_pwd, width=16)
pwd_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
