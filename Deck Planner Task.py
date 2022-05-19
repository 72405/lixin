from tkinter import *

def quit():
    main_window.destroy()

def calculate_deck():
    global entry_deck_length
    global entry_deck_width
    global entry_deck_height 
    Label(main_window, text="Area").grid(column=0,row=4)
    deck_area = int(entry_deck_length.get())* int(entry_deck_width.get())
    Label(main_window, text=deck_area).grid(column=1,row=4, sticky=W)    

    Label(main_window, text="Posts").grid(column=0,row=5)
    deck_posts = (int(entry_deck_length.get()) + 1)* int(entry_deck_width.get())
    Label(main_window, text=deck_posts).grid(column=1,row=5, sticky=W)

    Label(main_window, text="Post Length").grid(column=0,row=6)
    if int(entry_deck_height.get()) <= 1:
        post_length = 1.8
    else:
        post_length = 2.4
    Label(main_window, text=post_length).grid(column=1,row=6, sticky=W)

    Label(main_window, text="Cement Bags").grid(column=0,row=7)
    cement_bags = deck_posts
    Label(main_window, text=cement_bags).grid(column=1,row=7, sticky=W)

    Label(main_window, text="Bearers").grid(column=0,row=8)
    length_bearers = deck_area * 2
    Label(main_window, text=length_bearers).grid(column=1,row=8, sticky=W)

    Label(main_window, text="Joists").grid(column=0,row=9)
    joist_length = deck_area / .4
    Label(main_window, text=joist_length).grid(column=1,row=9, sticky=W)

    Label(main_window, text="Decking").grid(column=0,row=10)
    decking_length = deck_area * 11
    Label(main_window, text=decking_length).grid(column=1,row=10, sticky=W)

def main():
    global main_window
    global entry_deck_length
    global entry_deck_width
    global entry_deck_height  
    main_window =Tk()
    Button(main_window, text="Quit",command=quit) .grid(column=0, row=0)
    Button(main_window, text="Calculate",command=calculate_deck) .grid(column=1,row=0)
    
    Label(main_window, text="Length").grid(column=0,row=1)
    entry_deck_length = Entry(main_window)
    entry_deck_length.grid(column=1,row=1,padx=10,pady=5)
    
    Label(main_window, text="Width").grid(column=0,row=2)
    entry_deck_width = Entry(main_window)
    entry_deck_width.grid(column=1,row=2,padx=10,pady=5)
    
    Label(main_window, text="Height").grid(column=0,row=3)
    entry_deck_height = Entry(main_window)
    entry_deck_height.grid(column=1,row=3,padx=10,pady=5)
    main_window.mainloop()
    
main()
