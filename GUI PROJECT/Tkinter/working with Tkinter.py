from tkinter import *
from tkinter import filedialog, messagebox

windows = Tk()
windows.geometry("600x600")
windows.config(background="red")
windows.title("Tkinter Practice")

# def createwidget():
#     link1_label = Label(windows,text="Youtube Downloader",font=("Arials",10,"bold"),bg="light blue",fg="black")
#     link2_label = Label(windows,text="Created by (Jwhyte)",font=("arial",9,"bold"),bg="lightgreen",fg="black")
#     link1_label.grid(row=0, column=2, pady=5, padx=5)
#     link2_label.grid(row=1, column=2, pady=1, padx=1)



spin = Spinbox(windows,from_=1900,to=2022)
spin.pack()

# createwidget()
windows.mainloop()