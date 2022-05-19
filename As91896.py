from tkinter import * # imports everything from Tk-tkinter is a module
from tkinter import ttk # ttk is a sub module of tkinter

root = Tk() # top level window

# Create a Label Widget
label = Label(root, text="Hello Python") # wha
# font colour ,config is for properties
label.config(text="Hello Python", fg="red")
label.config(bg="yellow") # background colour
label.config(font ='Times 20')

label.config(text='Python is a great program.')
label.config(wraplength='150') # wrap text if long label
label.config(justfiy="right")

# Showing it on the screen
label.pack()
root.geometry("300x250")

root.mainloop() 
