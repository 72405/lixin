from tkinter import * # imports

root = Tk() # top level window
def callback():
    label.config(text='You click me!',fg='red',bg='yellow')

label = Label(root, text = "Hello python")
label.pack()


button = Button(root, text = 'Click me!',command=callback)
button['state']='disabled'
button['state']='normal'
button.pack()

root.geometry("350x300")
root.mainloop()
