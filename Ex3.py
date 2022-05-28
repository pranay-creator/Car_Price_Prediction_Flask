from tkinter import *

class MyButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Click Me", command=self.printMessage)
        self.printButton.pack()
        
        self.quit = Button(frame, text="Quit", command=win.destroy)
        self.quit.pack()

    def printMessage(self):
        print("This is My Button Class")

win = Tk()
win.geometry("250x250")
b = MyButton(win)

win.mainloop()