import pyshorteners
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Сокращатель ссылок')
root.geometry('400x150')
root.resizable(width=False, height=False)

linkLabel = Label(root, text='Вставте ссылку')
linkLabel.place(x=10, y=10)



root.mainloop()
