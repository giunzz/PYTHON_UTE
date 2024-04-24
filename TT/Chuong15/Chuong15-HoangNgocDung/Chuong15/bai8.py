from tkinter import *
from math import *
main = Tk()
main.title('Bai8')


def divisor():
    n = int(num1.get())
    tmp =""
    for i in range(1,n+1):
        if n % i == 0:
            tmp += str(i) + " "
    Label(main, text = "The divisors of N: " + tmp).grid(row=2)
    # num1.delete(0,END)

main.geometry('500x100')
Label(main,text="Enter the Value of N:").grid(row = 0)


num1 = Entry(main)


num1.grid(row=0, column=1)


# Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='Validate', command=divisor).grid(row=4, column=0, sticky=W,)

mainloop()