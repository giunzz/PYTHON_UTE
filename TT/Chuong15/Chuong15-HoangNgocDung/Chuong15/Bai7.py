from tkinter import *
from math import *
main = Tk()
main.title('Bai7')


def calc():
    blank.delete(0, END)
    Ans = int(num1.get()) * 2
    blank.insert(0, Ans)


main.geometry('500x100')
Label(main,text="Enter the Value of N:").grid(row = 0)
Label(main, text = "Here is the double 2 *N:").grid(row=2)


num1 = Entry(main)
blank = Entry(main)


num1.grid(row=0, column=1)
blank.grid(row=2, column=1)


# Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='Validate', command=calc).grid(row=4, column=0, sticky=W,)

mainloop()