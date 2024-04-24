from tkinter import *
from math import *
main = Tk()
main.title('Bai9')

def uc():
    blank.delete(0, END)
    Ans = gcd(int(num1.get()), int(num2.get()))
    blank.insert(0, Ans)

def bc():
    blank.delete(0, END)
    a = int(num1.get())
    b = int(num2.get())
    Ans = abs(a*b) // gcd(a,b)
    blank.insert(0, Ans)


main.geometry('500x100')
Label(main, text = "Enter the value of m:").grid(row=0)
Label(main, text = "Enter the value of n:").grid(row=1)
Label(main, text = "The Answer is:").grid(row=2)



num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)

Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='GCD', command=uc).grid(row=4, column=3, sticky=W)
Button(main, text='LCM', command=bc).grid(row=4, column=4, sticky=W)

mainloop()