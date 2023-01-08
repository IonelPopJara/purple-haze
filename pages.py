from tkinter import Frame
import tkinter as tk
import utils
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

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

        currentPollutionButton = tk.Button(self, text="Current Pollution Data", command= lambda: self.showCurrentPollutionPage(e1.get()), width=20, font=DEFAULTFONT)
        currentPollutionButton.place(x=130, rely=0.4, anchor="center")

        averagePollutionButton = tk.Button(self, text="Average Pollution Data", command= lambda : self.showAveragePollutionPage(e1.get()), width=20, font=DEFAULTFONT)
        averagePollutionButton.place(x=370, rely=0.4, anchor="center")

    def showCurrentPollutionPage(self, cityName):
        self.controller.show_frame(CurrentPollutionPage)
        page = self.controller.get_page(CurrentPollutionPage)
        page.updatePage(cityName)
    
    def showAveragePollutionPage(self, cityName):
        self.controller.show_frame(AveragePollutionPage)
        page = self.controller.get_page(AveragePollutionPage)
        page.updatePage(cityName)


class CurrentPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.cityNameLabel = tk.Label(self, text="City Name", font=DEFAULTFONT)
        self.cityNameLabel.pack()

        self.aqiLabel = tk.Label(self, text="Air Quality", font=DEFAULTFONT)
        self.aqiLabel.pack()

        backButton = tk.Button(self, text="Go Back", command= self.goBack)
        backButton.pack()

        self.canvas = FigureCanvasTkAgg()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
    
    def updatePage(self, cityName):
        plt.close('all')
        self.canvas.get_tk_widget().pack_forget() # This cleans the canvas
        
        try:
            lat, lon = utils.get_location_coordinates(city_name=cityName)
            print(lat, lon)
            self.cityNameLabel.config(text=cityName.capitalize())

            aqi, components = utils.get_current_pollution_data(lat, lon)
            print(aqi, components)
            self.aqiLabel.config(text=f'Air Quality: {aqi}')

            utils.plot(self, title="Air Quality", city_name=cityName, data=components)

        except:
            print("Something went wrong")
            self.cityNameLabel.config(text="City not found")
            self.aqiLabel.config(text="Try again")
    
    def goBack(self):
        self.controller.show_frame(MainPage)


class AveragePollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="aaaaa", font=DEFAULTFONT)
        self.label.grid(row=0, column=0, padx=10, pady=10, columnspan= 3)

        backButton = tk.Button(self, text="Go Back", command= self.goBack)
        backButton.grid(row=1, column=0, padx=10, pady=10)
    
    def updatePage(self, cityName):
        self.label.config(text=cityName)

    def goBack(self):
        self.controller.show_frame(MainPage)