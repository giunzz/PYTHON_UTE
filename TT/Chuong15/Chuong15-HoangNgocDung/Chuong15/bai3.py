from tkinter import *

def callback():
    num_value = eval(entry.get())
    ans = 1
    for i in range(1, num_value+1):
        ans *= i
    output.configure(text = 'The factorial of {} is {}! = {}'.format(num_value, num_value, ans))
    entry.delete(0,END)


root = Tk()
text = Label(text = 'Enter value of integer N: ',font=('Verdana', 16))
output = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=20)
calc_button = Button(text='Validate', font=('Verdana', 16), width= 20 ,command=callback)

text.grid(row = 0, column = 0)
entry.grid(row=0, column=1)
calc_button.grid(row=2, column=1)
output.grid(row=1, column=1)


mainloop()