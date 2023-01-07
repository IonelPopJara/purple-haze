from tkinter import Frame
from tkinter import ttk

DEFAULTFONT = ("Roboto", 35)

class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(self, text="Purple Haze", font=DEFAULTFONT)

        label.grid(row=0, column=0, padx=10, pady=10)

        currentPollutionButton = ttk.Button(self, text="Current Pollution Data", command= lambda : controller.show_frame(CurrentPollutionPage))
        currentPollutionButton.grid(row=1, column=0, padx=10, pady=10)

        historicalPollutionButton = ttk.Button(self, text="Historical Pollution Data", command= lambda : controller.show_frame(HistoricalPollutionPage))
        historicalPollutionButton.grid(row=2, column=0, padx=10, pady=10)

class CurrentPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(self, text="Current Pollution Data", font=DEFAULTFONT)

        label.grid(row=0, column=0, padx=10, pady=10)

        backButton = ttk.Button(self, text="Back", command= lambda : controller.show_frame(MainPage))
        backButton.grid(row=1, column=0, padx=10, pady=10)

class HistoricalPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(self, text="Historical Pollution Data", font=DEFAULTFONT)

        label.grid(row=0, column=0, padx=10, pady=10)

        backButton = ttk.Button(self, text="Back", command= lambda : controller.show_frame(MainPage))
        backButton.grid(row=1, column=0, padx=10, pady=10)