from tkinter import * # imports everything from Tk-tkinter is a module

root = Tk() # top level window

#Create Label
label = Label(root,text = "Hello Pyhton")
label.pack()

#Create button(without command does not do any!)
button= Button(root, text = 'Click me!')
button.pack()

root.geometry("350x300")
root.mainloop()


