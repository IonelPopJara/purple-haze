from tkinter import Frame, Label, Entry, Button
import utils

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

TITLE = ("Helvetica", 25)
DEFAULTFONT = ("Helvetica", 15)

class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        label = Label(self, text="Welcome to Purple Haze", font=TITLE)

        label.place(relx=0.5, rely=0.2, anchor="center")

        e1 = Entry(self, font=DEFAULTFONT)
        e1.place(relx=0.5, rely=0.3, anchor="center")
        e1.insert(0, "Enter a city name")
        e1.focus_set()

        currentPollutionButton = Button(self, text="Current Pollution Data", command= lambda: self.showCurrentPollutionPage(e1.get()), width=20, font=DEFAULTFONT)
        currentPollutionButton.place(relx=0.5, rely=0.4, anchor="center")

    def showCurrentPollutionPage(self, cityName):
        self.controller.show_frame(CurrentPollutionPage)
        page = self.controller.get_page(CurrentPollutionPage)
        page.updatePage(cityName)


class CurrentPollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.cityNameLabel = Label(self, text="City Name", font=TITLE)
        self.cityNameLabel.pack()

        self.aqiLabel = Label(self, text="Air Quality Index", font=DEFAULTFONT)
        self.aqiLabel.pack()

        backButton = Button(self, text="Go Back", command= self.goBack)
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
            self.aqiLabel.config(text=f'Air Quality Index: {aqi}')

            utils.plot(self, title="Air Quality", city_name=cityName, data=components)

        except:
            print("Something went wrong")
            self.cityNameLabel.config(text="City not found")
            self.aqiLabel.config(text="Try again")
    
    def goBack(self):
        self.controller.show_frame(MainPage)