from tkinter import *
from math import *
import string
main = Tk()
main.title('Bai1')


def printext():
    s = num.get()
    s = s[::-1]
    Label(main, text = s).grid(row=2,column=1)
    # num1.delete(0,END)

main.geometry('500x100')
Label(main,text="Enter a word").grid(row = 0)
num = Entry(main)
num.grid(row=0, column=1)


Button(main, text='Validate', command=printext).grid(row=5, column=0, sticky=W,)

mainloop()