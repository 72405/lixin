from tkinter import *
root = Tk()

root.title("Frames")

frame = Frame(root, height=300, width=300, bg='red',bd=7, relief=SUNKEN)
frame.pack(fill=X)

button1 = Button(frame,text='Button1')
button2 = Button(frame,text='Button1')

button1.pack(side=LEFT, padx=20, pady=50)
button2.pack(side=LEFT, padx=20, pady=50)

searchBar = LabelFrame(root, text='Search Box')

search_txt = Label(root, text="Search: ")
search_input = Entry(root, width=30)

button3 = Button(root, text='Search')
searchBar.place(x=100, y=20)

search_txt.place(x=20, y=80)
button3.place(x=250, y=150)

root.geometry('650x650+450+200')
root.mainloop()

