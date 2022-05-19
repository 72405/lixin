from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

entry.insert(0,'Please enter your name')
entry2.insert(0,'Please enter your password')

button = ttk.Button(root, text='Enter')
lbltitle = ttk.Label(text='Our Titile here', font=(('Arial'),30))
lblname = ttk.Label(text='Your name: ')
lblpass = ttk.Label(text='Your Password: ')

lbltitle.grid(row=0, column=0,columnspan=2,pady=10)
lblname.grid(row=1, column=0,sticky=W)
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1,sticky=E+W)

root.geometry('500x450')
root.mainloop()
