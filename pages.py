from tkinter import Frame
import tkinter as tk

DEFAULTFONT = ("Helvetica", 15)
TITLE = ("Helvetica", 25)

class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        label = tk.Label(self, text="Welcome to Purple Haze", font=TITLE)

        label.place(relx=0.5, rely=0.2, anchor="center")

        e1 = tk.Entry(self, font=DEFAULTFONT)
        e1.place(relx=0.5, rely=0.3, anchor="center")
        e1.insert(0, "Enter a city name")
        e1.focus_set()

        # currentPollutionButton = tk.Button(self, text="Current Pollution Data", command= lambda : controller.show_frame(CurrentPollutionPage), width=20, font=DEFAULTFONT)
        currentPollutionButton = tk.Button(self, text="Current Pollution Data", command= lambda: self.showCurrentPollutionPage(e1.get()), width=20, font=DEFAULTFONT)
        currentPollutionButton.place(x=130, rely=0.4, anchor="center")

        # averagePollutionButton = tk.Button(self, text="Average Pollution Data", command= lambda : controller.show_frame(HistoricalPollutionPage), width=20, font=DEFAULTFONT)
        # averagePollutionButton.place(x=370, rely=0.4, anchor="center")
    
    def showCurrentPollutionPage(self, cityName):
        self.controller.show_frame(CurrentPollutionPage)
        page = self.controller.get_page(CurrentPollutionPage)
        page.updatePage(cityName)


class CurrentPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
    
    def updatePage(self, cityName):
        self.__init__(self)
        label = tk.Label(self, text=cityName, font=DEFAULTFONT)
        label.grid(row=0, column=0, padx=10, pady=10, columnspan= 3)

        backButton = tk.Button(self, text="Go Back", command= self.goBack)
        backButton.grid(row=1, column=0, padx=10, pady=10)
    
    def goBack(self):
        self.controller.show_frame(MainPage)


class HistoricalPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # label = tk.Label(self, text="Historical Pollution Data", font=DEFAULTFONT)

        # label.grid(row=0, column=0, padx=10, pady=10)

        # backButton = tk.Button(self, text="Back", command= lambda : controller.show_frame(MainPage))
        # backButton.grid(row=1, column=0, padx=10, pady=10)