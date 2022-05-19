from tkinter import *
from tkinter import ttk

root = Tk()

def callback():
    print("Your name :"+entry.get())
    print("Your Password :"+entry2.get())
    if chavr.get() ==1:
        print("Remember me selected")
    else:
        print("not selected")
    print(gender.get())

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name: ")
entry2.insert(0, "Please enter your password: ")

button = ttk.Button(root, text='Enter')
button.config(command=callback)

lbltitle = ttk.Label(text='Our title', font=(('Arial'), 22))

lblname = ttk.Label(text='Your name :')
lblpass = ttk.Label(text='Your Password : ')
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

chvar = IntVar()
chvar.set(0)

gender = StringVar()

ttk.Radiobutton(root,text='Female', value='Female',
                var=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text='Male', value='Male',
                var=gender).grid(row=5, column=1)

cbox = Checkbutton(root, text='Remember Me', variable=chvar,
                   font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2)

months = StringVar()

numbers = []
for i in range(0,10):
    numbers.append(i)
    
comboBox = ttk.Combobox(root, textvariable=months,
                        values=(numbers),state='readonly').grid(row=6, column=0)

year = StringVar()
Spinbox(root, from_=1990, to=2822, textvariable=year).grid(row=6, column=1)

root.geometry("500x450")
root.mainloop()
