from tkinter import *
from tkinter import ttk
import random


# window.title("dice roll app")
#
# window.geometry("400x400")


class DandDDice(object):

    def __init__(self, parent):
        parent.title('D&D dice roller')
        parent.geometry('250x200')

        self.fourside = StringVar()
        self.sixside = StringVar()
        self.twentyside = StringVar()

        self.mainFrame = ttk.Frame(parent)
        self.mainFrame.grid()

        self.foursided = ttk.Button(self.mainFrame, text='d4', command=self.d4)
        self.foursided.grid(row=0, column=0, padx=10, pady=10)
        self.fourresult = ttk.Label(self.mainFrame, textvariable=self.fourside)
        self.fourresult.grid(row=0, column=1, padx=10, pady=10)

        self.sixsided = ttk.Button(self.mainFrame, text='d6', command=self.d6)
        self.sixsided.grid(row=2, column=0, padx=10, pady=10)
        self.sixresult = ttk.Label(self.mainFrame, textvariable=self.sixside)
        self.sixresult.grid(row=2, column=1, padx=10, pady=10)

        self.twentysided = ttk.Button(self.mainFrame, text='d20', command=self.d20)
        self.twentysided.grid(row=3, column=0, padx=10, pady=10)
        self.twentyresult = ttk.Label(self.mainFrame, textvariable=self.twentyside)
        self.twentyresult.grid(row=3, column=1, padx=10, pady=10)

    def d4(self):
        four = random.randint(1, 4)
        self.fourside.set(four)

    def d6(self):
        six = random.randint(1, 6)
        self.sixside.set(six)

    def d20(self):
        twenty = random.randint(1, 20)
        self.twentyside.set(twenty)



root = Tk()
dice = DandDDice(root)
root.mainloop()

