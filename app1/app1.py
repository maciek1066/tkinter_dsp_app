import random
import tkinter as tk

window = tk.Tk()

window.title("Greetings")

window.geometry("400x200")


# FUNCTIONS
def phrase_generator():
    phrases = ["Hello ", "Nice to see you "]

    name = str(entry1.get())

    return phrases[random.randint(0, 1)] + name


def phrase_display():
    greeting = phrase_generator()

    greeting_display = tk.Text(master=window, height=10, width=40)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)


# LABEL
label1 = tk.Label(text="Welcome")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name? ")
label2.grid(column=0, row=1)

# ENTRY FIELD
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# BUTTON
button1 = tk.Button(text="click", command=phrase_display)
button1.grid(column=0, row=2)


window.mainloop()

