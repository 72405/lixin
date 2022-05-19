from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your name is :" +val1)
    print("Your password is :" +val2)Width

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root,width=30)
entry.insert(0,"Please enter your name")
entry2.config(show='#')

button=ttk.Button(root,text='Click me!',command=callback)

entry.pack()
entry2.pack()
button.pack()

root.geometry("350x300")
root.mainloop()
