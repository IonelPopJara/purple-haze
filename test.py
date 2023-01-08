from tkinter import Tk
import matplotlib.pyplot as plt

from pages import *

class PurpleHazeApp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.geometry("500x700")
        self.resizable(False, False)

        self.frames = {}

        for F in (MainPage, CurrentPollutionPage, AveragePollutionPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def get_page(self, page_class):
        return self.frames[page_class]
    
    def quit_app(self):
        self.destroy()

def on_closing():
    plt.close("all")
    app.destroy()


app = PurpleHazeApp()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.wm_title("Purple Haze")

app.mainloop()