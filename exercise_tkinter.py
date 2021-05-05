import tkinter as tk
from tkinter import *

window = Tk()

window.geometry("500x500")  # positioning the size of the window
window.title("Adding Numbers")

#authorize
num1 = StringVar()
num2 = StringVar()
result = StringVar()

def adding_inputs():
    one = int(first_num_entry.get())
    two = int(second_num_entry.get())
    ans = one + two
    return result.set(ans)


def clear_inputs():
    first_num_entry.delete(0, END)
    second_num_entry.delete(0, END)
    answer_entry.config(state="normal")
    answer_entry.delete(0, END)
    answer_entry.config(state="readonly")
def exit_program():
    return window.destroy()

#Labels for Widget
first_num=Label(window,text="Enter your first number : ")
second_num=Label(window,text="Enter second number : ")
answer=Label(window, text="Your answer" )

#Entrys for Widget
first_num_entry=Entry(window, textvariable = num1)
second_num_entry=Entry(window , textvariable = num2)
answer_entry=Entry(window , textvariable = result , state = DISABLED)

#Buttons for Widget
add = Button(window, text="Add" , command = adding_inputs)
clear = Button(window, text="Clear" , command = clear_inputs)
exit = Button(window, text="Exit" , command = exit_program )

#Putting the widget and displaying it
first_num.place(x=0, y=0)
second_num.place(x=0, y=25)
answer.place(x=0, y=50)

#Placing Entries
first_num_entry.place(x=250, y=0)
second_num_entry.place(x=250, y=25)
answer_entry.place(x=250, y=50)

#Placing Buttons
add.place(x=125, y=75)
clear.place(x=175, y=75)
exit.place(x=225, y=75)
#proceeding with putting it on the screen
window.mainloop()