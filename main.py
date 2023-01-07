from tkinter import Tk, messagebox, Button

top = Tk()
top.geometry("250x250")
top.resizable(False, False)

def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello World")

currentPollutionButton = Button(top, text="Show current pollution data", command=helloCallBack)
currentPollutionButton.place(x=50, y=50)

historicalPollutionButton = Button(top, text="Show historical pollution data", command=helloCallBack)
historicalPollutionButton.place(x=50, y=100)

top.mainloop()