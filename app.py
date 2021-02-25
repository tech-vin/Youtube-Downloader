from tkinter import *
from pytube import YouTube
from tkinter import messagebox


def download():
    url = YouTube(str(url_box.get()))
    video = url.streams.first()
    video.download()    
    messagebox.showinfo('', 'Download completed!')

root = Tk()
root.title('Youtube Downloader')
root.geometry('400x300')

frame = Frame(root, bg='#6ca128')
frame.pack(expand=True, fill=BOTH)

url_box = Entry(
    frame,
    width=30,
    font=('Arial',14)
    )
url_box.pack(pady=40)

download_btn = Button(
    frame,
    text='DOWNLOAD',
    font=('Arial', 24),
    command=download
)

download_btn.pack()

root.mainloop()