from tkinter import *

def callback():
    num_value1 = eval(entry1.get())
    num_value2 = eval(entry2.get())
    ans = num_value1 + num_value2
    output.configure(text = 'The Sum is : {} + {} = {}'.format(num_value1, num_value2, ans))
    entry1.delete(0,END)
    entry2.delete(0,END)


root = Tk()

text1 = Label(text = 'Enter value of M: ',font=('Verdana', 16), width = 20)
text2 = Label(text = 'Enter value of N: ',font=('Verdana', 16), width = 20)
output = Label(font=('Verdana', 16))
entry1 = Entry(font=('Verdana', 16), width=20)
entry2 = Entry(font=('Verdana', 16), width=20)
calc_button = Button(text='Validate', font=('Verdana', 16), command=callback)

text1.grid(row = 0, column = 0)
entry1.grid(row=0, column=1)
text2.grid(row = 1, column =0)
entry2.grid(row=1, column=1)
calc_button.grid(row=4, column=2, columnspan = 2)
output.grid(row=3, column=1)


mainloop()