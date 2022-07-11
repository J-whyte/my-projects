import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

def createWidgets():
    link_label = Label(root, text="Youtube Url: ", bg="white")

root = tk.Tk()

root.geometry("600x600")
# root.resizable(False,False)
root.title("YOUTUBE DOWNLOADER BY (Jwhyte)")
root.config(background="Red")

youtube_logo = PhotoImage(file="youtube downloader.png")
root.iconphoto(False,youtube_logo)

Label(root,text="Video Downloader",font=("Arial",30 ,"bold"),fg="black",bg="Lightblue").pack(padx=5,pady=50)

video_link = StringVar()
Label(root,text="Enter the link: ",font=("Arial",25,"bold")).place(x=170,y=150)

entry_link = Entry(root,textvariable=video_link,bd=4,width=55,font=40).place(x=30,y=200)


def video_download():
    video_url = YouTube(str(video_link.get()))
    videos=video_url.streams.first()
    videos.download()

    Label(root, text="Download Completed !!",font=("Arial",20,"Bold"),bg="lightpink",fg="black").place(x=120,y=350)
    Label(root,text="Check out your Project folder",font=("Arial",25,"Bold"),bg="yellow").place(x=130 ,y=500 )


Button(root,text="DOWNLOAD",font=("Arial",25,"bold"),bg="lightblue",command=video_download).place(x=180,y=300)





root.mainloop()