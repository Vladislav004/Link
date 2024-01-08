import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox


def short():
    s = pyshorteners.Shortener()
    shor = beforeLink.get()
    afterLink.delete(0, END)
    afterLink.insert(0, s.tinyurl.short(shor))


root = Tk()
root.title('Сокращатель ссылок')
root.geometry('400x150')
root.resizable(width=False, height=False)

beforelinkLabel = Label(root, text='Вставте ссылку')
beforelinkLabel.place(x=10, y=10)

beforeLink = ttk.Entry(root, width=40, font='Arial 13')
beforeLink.place(x=10, y=30)

btn = ttk.Button(root, text='Сократить', command=short)
btn.place(relx=0.5, y=80, anchor=CENTER)

afterLinkLabel = Label(root, text='Результат')
afterLinkLabel.place(x=10, y=85)

afterLink = ttk.Entry(root, width=40, font='Arial 13')
afterLink.place(x=10, y=105)

root.mainloop()
