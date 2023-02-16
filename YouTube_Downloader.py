import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

root = tk.Tk()
root.geometry("600x250+400+30")
root.resizable(False,False)
root.title("YouTube Video Downloader -by Josh")
root.config(background="#154c79")

video_link = StringVar()
download_path = StringVar()

image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

photo=PhotoImage(file="logo.png")
myimage=Label(image=photo,background='#154c79')
myimage.place(x=5, y=5)

# body_label = Label(root, text="by Josh", font="Candara 11", background="#154c79", foreground="white").place(x=350, y=50)

def widgets():
    head_label = Label(root, text="YouTube Downloader", font="Candara 16", background="#154c79", foreground="white",
    padx=15, pady=15)

    head_label.grid(row=1, column=1,padx=5,pady=10,columnspan=3)

    link_label = Label(root, text="Paste YouTube Link:", bg="#154c79", fg="white", padx=5, pady=5)

    link_label.grid(row=2, column=0,padx=5, pady=5,)

    root.linkText=Entry(root, width=30, textvariable=video_link, font="Arial 14")

    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Save At", bg="#154c79", fg="white", padx=9, pady=5)

    destination_label.place(x=3, y=125)

    root.destinationText = Entry(root, width=30, textvariable=download_path, font="Arial 14")

    root.destinationText.grid(row=3, column=1,padx=5, pady=5)

    browse_B = Button(root, text="Browse", command=Browse, width=16, background="#eeeee4",relief=GROOVE)

    browse_B.place(x=472, y=124)

    browse_B = Button(root, text="Download Video", command=Download, width=15, background="#eeeee4", relief=GROOVE)
    browse_B.place(x=250, y=180)

    # browse_B.grid(row=1, column=1, pady=20, padx=20)

def Browse():
    download_dir = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_path.set(download_dir)

def Download():
    YouTube_link = video_link.get()

    download_folder = download_path.get()

    getvideo = YouTube(YouTube_link)

    videostream = getvideo.streamss.first()

    videostream.download(download_folder)

    messagebox.showinfo("SUCCEFULLY SAVED VIDEO TO\n" + download_folder)

widgets()

root.mainloop()

    
