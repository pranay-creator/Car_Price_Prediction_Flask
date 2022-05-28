from tkinter import *

win = Tk()

def leftclick(event):
    print("Left Button Click")

def rightclick(event):
    print("Right Button Click")


frame = Frame(win, width=300, height=300)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-3>",rightclick)
frame.pack()

win.mainloop()