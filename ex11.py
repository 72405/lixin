from tkinter import *
root = Tk()

titile = Label(root, text="Place Geometry Manager",
               font=(("Verdana"), 15))
name_txt = Label(root, text="Name :")
pass_txt = Label(root, text="Password :")
name_input = Entry(root, width=30)
pass_input = Entry(root, width=30)

name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)
pass_txt.place(x=20, y=110)
pass_input.place(x=100, y=110)

Button.place(x=250, y=150)

root.geometry("450x450+650+350")
root.mainloop()

