from tkinter import*

win = Tk()

win.geometry("250x250")

def hello():
    print("Welcome to AI Class!!!")

label = Label(win, text = "This is my first GUI")
label.pack()

button1 = Button(win, text="Button1", fg="red", command=hello)
button1.pack()

button2 = Button(win, text="Button2", fg="red")
button2.pack()

win.mainloop()