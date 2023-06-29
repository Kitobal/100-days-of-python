import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


def button_click():
    miles = float(my_input.get())
    result = miles * 1.60934
    res_label.config(text=f"{round(result, 2)}")


# input
my_input = tkinter.Entry()
my_input.grid(row=0, column=1)

# input label
inp_label = tkinter.Label(text="Miles", font=("Arial", 12))
inp_label.grid(row=0, column=2)

# equals label
equal_label = tkinter.Label(text="Is equal to: ", font=("Arial", 12))
equal_label.grid(row=1, column=0)

# result label
res_label = tkinter.Label(text="0", font=("Arial", 12))
res_label.grid(row=1, column=1)

# output label
km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(row=1, column=2)

# button
button = tkinter.Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)

window.mainloop()
