from tkinter import *
from math import *
main = Tk()
main.title('Bai2')


def tinhtong():
    n = int(num1.get())
    s = n * (n + 1) // 2
    tmp = 'The num is 1 '
    for i in range(2, n//2):
        tmp += '+ ' + str(i)
    if (n != 1): tmp += '+...+ ' + str(n)
    Label(main, text = tmp + " is " + str(s)).grid(row=2,column=1)
    # num1.delete(0,END)

main.geometry('500x100')
Label(main,text="Enter the Value of N:").grid(row = 0)
num1 = Entry(main)
num1.grid(row=0, column=1)



# Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W)
Button(main, text='Validate', command=tinhtong).grid(row=5, column=0, sticky=W,)

mainloop()