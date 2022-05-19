from tkinter import * 
from tkinter import ttk
root = Tk()
root.geometry("500x400")

button1 = Button(root, text = "Click me!")
button2 = ttk.Button(root, text = "Click me!")
button1.pack()
button2.pack()


root.mainloop()
