from tkinter import Frame, Label, Entry, Button
import utils

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

TITLE = ("Helvetica", 25)
DEFAULTFONT = ("Helvetica", 15)

matplotlib.use('TkAgg')

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

        currentPollutionButton = Button(self, text="Current Pollution Data", command= lambda: self.show_pollution_page(e1.get()), width=20, font=DEFAULTFONT)
        currentPollutionButton.place(relx=0.5, rely=0.4, anchor="center")

    def show_pollution_page(self, cityName):
        self.controller.show_frame(PollutionPage)
        page = self.controller.get_page(PollutionPage)
        page.update_page(cityName)

class PollutionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        self.cityNameLabel = Label(self, text="City Name", font=TITLE)
        self.cityNameLabel.pack()

        self.aqiLabel = Label(self, text="Air Quality Index", font=DEFAULTFONT)
        self.aqiLabel.pack()

        backButton = Button(self, text="Go Back", command= lambda: self.controller.show_frame(MainPage))
        backButton.pack()

        self.canvas = FigureCanvasTkAgg()
    
    def update_page(self, cityName):

        plt.close('all')
        # This cleans the canvas
        self.canvas.get_tk_widget().pack_forget()
        
        try:
            lat, lon = utils.get_location_coordinates(city_name=cityName)
            print(lat, lon)
            self.cityNameLabel.config(text=cityName.capitalize())

            aqi, components = utils.get_current_pollution_data(lat, lon)
            print(aqi, components)
            self.aqiLabel.config(text=f'Air Quality Index: {aqi}')

            utils.embed_plot(self, title="Air Quality", city_name=cityName, data=components)

        except:
            print("Something went wrong")
            self.cityNameLabel.config(text="City not found")
            self.aqiLabel.config(text="Try again")