from tkinter import *

def callback():
    num_value = eval(entry.get())
    flag = 0
    if num_value >= 0:
        sqrt_n = int(num_value ** 0.5)
        if sqrt_n * sqrt_n == num_value:
            flag = 1
    if flag == 0:
        output.configure(text = '{} is not a perfect square'.format(num_value))
    else:
        output.configure(text = '{} is a perfect square {} = {} ^ 2'.format(num_value, num_value, round(num_value ** 0.5)))
    entry.delete(0,END)


root = Tk()

text = Label(text = 'Enter value of integer N: ',font=('Verdana', 16))
output = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=20)
calc_button = Button(text='Validate', font=('Verdana', 16), width = 20 ,command=callback)

text.grid(row = 0, column = 0)
entry.grid(row=0, column=1)
calc_button.grid(row=1, column=1)
output.grid(row=2, column=1)


mainloop()