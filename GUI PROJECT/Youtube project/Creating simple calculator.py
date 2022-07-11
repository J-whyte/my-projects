from tkinter import *
from tkinter import  messagebox,filedialog
root = Tk()
root.title("Simple Calculator")
entry = Entry(root,width=58,borderwidth=3)
entry.grid(row=0,column=0,columnspan=4,pady=5,padx=5)

def button_click(number ):
    # entry.delete(0,END)
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_number = entry.get()
    global f_number
    global math
    math = "addition"
    f_number = int(first_number)
    entry.delete(0,END)


def button_equal():
    second_number = entry.get()
    entry.delete(0,END)

    if math =="addition":
        entry.insert(0,f_number + int(second_number))
    if math == "Subtraction":
        entry.insert(0,f_number - int(second_number))
    if math == "Multiplication":
        entry.insert(0,f_number * int(second_number))
    if math == "Division":
        entry.insert(0,f_number / int(second_number))


def button_subtract():
    first_number = entry.get()
    global f_number
    global math
    math = "Subtraction"
    f_number = int(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_number
    global math
    math = "Division"
    f_number = int(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_number
    global math
    math = "Multiplication"
    f_number = int(first_number)
    entry.delete(0, END)


def button_percent():
    first_number = entry.get()
    global f_number
    global math
    math = "addition"
    f_number = int(first_number)
    entry.delete(0, END)


def button_dot():
    first_number = entry.get()
    global f_number
    global math
    math = "addition"
    f_number = int(first_number)
    entry.delete(0, END)


def about():
    messagebox.showinfo("About Software","""This is a simple calculator used for calculating simple arithmetic.This software was created by Jwhyte.\nsoftware created on the 20/01/2022""")


# Define button
button_1 = Button(root,text="1",pady=20,padx=40, command=lambda: button_click(1))
button_2 = Button(root,text="2",pady=20,padx=40, command=lambda:button_click(2))
button_3 = Button(root,text="3",pady=20,padx=40, command=lambda:button_click(3))
button_4 = Button(root,text="4",pady=20,padx=40,command=lambda:button_click(4))
button_5 = Button(root,text="5",pady=20,padx=40, command=lambda:button_click(5))
button_6 = Button(root,text="6",pady=20,padx=40, command=lambda:button_click(6))
button_7 = Button(root,text="7",pady=20,padx=40, command=lambda:button_click(7))
button_8 = Button(root,text="8",pady=20,padx=40, command=lambda:button_click(8))
button_9 = Button(root,text="9",pady=20,padx=40, command=lambda:button_click(9))
button_0 = Button(root,text="0", pady=20,padx=85,command=lambda:button_click(0))
button_add = Button(root,text="+",pady=20,padx=40,command=button_add)
button_clear = Button(root,text="Clear",pady=20,padx=30,command=button_clear)
button_Equal = Button(root,text="Equal", pady=20,padx=79,command=button_equal)
button_subtract = Button(root,text="-",font=("arials",11,"bold"),pady=20,padx=39,command=button_subtract)
button_divide = Button(root,text="/",pady=20,padx=40,command=button_divide)
button_multiply = Button(root,text="x",pady=20,padx=40,command= button_multiply)
button_percent = Button(root,text="%",pady=18,padx=40,command= button_percent)
button_dot = Button(root,text=".",pady=20,padx=40,font=("Arial",10,"bold") ,command= button_dot)
button_About = Button(root,text="About Calc",pady=18,padx=15,font=("Arial",9),command=about)

# Put the button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3,column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2,column=3)

button_clear.grid(row=1, column=0)
button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)
button_0.grid(row=4,column=0,columnspan=2)
button_dot.grid(row=4,column=2)


button_add.grid(row=4, column=3)
button_Equal.grid(row=5,column=2,columnspan=2)
button_divide.grid(row=1,column=3)
button_percent.grid(row=5,column=1)

button_About.grid(row=5,column=0)
root.mainloop()