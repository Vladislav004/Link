import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Сокращатель ссылок')
root.geometry('400x150')
root.resizable(width=False, height=False)

linkLabel = Label(root, text='Вставте ссылку')
linkLabel.place(x=10, y=10)

beforeLink = ttk.Entry(root, width=40, font='Arial 13')
beforeLink.place(x=10, y=30)

btn = ttk.Button(root, text='Сократить')
btn.place(relx=0.5, y=80, anchor=CENTER)



root.mainloop()
