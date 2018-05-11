import tkinter as tk

window = tk.Tk()

window.title("Greetings ______")

window.geometry("400x200")

# LABEL
label1 = tk.Label(text="Welcome")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name?")
label2.grid(column=0, row=1)

# BUTTON
button1 = tk.Button(text="Click")
button1.grid(column=0, row=2)

# ENTRY FIELD
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

window.mainloop()

