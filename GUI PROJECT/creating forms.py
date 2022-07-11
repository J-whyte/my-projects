from tkinter import *
root = Tk()
root.geometry("700x700")
root.title("Sign up")
root.config(background="lightblue")

clicked = StringVar()
clicked.set("Month")
r=IntVar()
def sign_up():
    first_name =Label(root,text="First Name: ",font=("arials",9,"bold"),bg="white",fg="black",)
    first_name.grid(row=0,column=0,pady=5,padx=5)
    first_entry = Entry(root,width=40,bd=4,)
    first_entry.grid(row=0,column=1,pady=1,padx=1)

    last_name = Label(root, text="Last Name: ", font=("arials", 9, "bold"), bg="white", fg="black", )
    last_name.grid(row=0, column=2, pady=5, padx=5)
    last_entry = Entry(root, width=40, bd=4, )
    last_entry.grid(row=0, column=3, pady=1, padx=1)

    date_of_birth = Label(root, text="Date of birth", font=("arials", 9, "bold"), bg="white", fg="black", )
    date_of_birth.grid(row=1, column=0, pady=5, padx=5)

    listbox = Scrollbar(root)
    listbox.grid(row=2,column=0)
    mylist =Listbox(root,yscrollcommand=listbox)


sign_up()


mainloop()