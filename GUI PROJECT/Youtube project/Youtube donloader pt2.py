import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

root = tk.Tk()
root.geometry("600x120")
root.resizable(False,False)
root.title("YOUTUBE DOWNLOADER BY (Jwhyte)")
root.config(background="black")
video_link = StringVar()
download_path=StringVar()
youtube_logo = PhotoImage(file="Youtube icon.png")
root.iconphoto(False,youtube_logo)


def createwidgets():

    link_label = Label(root,text="Youtube Url: ",bg="lightblue",fg="black",bd=4)
    link_label.grid(row=1,column=0,pady=5,padx=5)

    root.link_text = Entry(root,width=60,textvariable=video_link,bd=4)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="File Destination: ", bg="lightblue", fg="black",bd=4)
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=60, textvariable=download_path,bd=4)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_button = Button(root,text="Browse",font=("arials",9,"bold"),command=browse, width=13,bg="lightblue",fg="black",bd=4)
    browse_button.grid(row=2,column=2,pady=1,padx=1)

    download_button = Button(root,text="Download Video",command=download_video,width=15,font=("Arials",9,"bold"),fg="black" , bg="lightblue" , bd=4)
    download_button.grid(row=3,column=1,pady=3,padx=3)


def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory path")
    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download(folder)

    # folder = download_path.get()
    # video_url = YouTube(str(video_link.get()))
    # video = video_url.streams.first()
    # video.download(folder)

    messagebox.showinfo("Success!!! Download Successful !!""\nYou will find the video at\n"+folder )


createwidgets()


mainloop()
