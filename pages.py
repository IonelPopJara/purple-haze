from tkinter import Frame, Label, Entry, Button
import utils

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

TITLE = ("Lato bold", 25)
DEFAULTFONT = ("Lato", 15)

matplotlib.use('TkAgg')

class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.configure(background='#FDFFF7')

        label = Label(self, text="Welcome to Purple Haze", font=TITLE)
        label.place(relx=0.5, rely=0.3, anchor="center")
        label.configure(background='#FDFFF7', fg='#8D3C7E')

        e1 = Entry(self, font=DEFAULTFONT)
        e1.place(relx=0.5, rely=0.45, anchor="center")
        e1.insert(0, "Enter a city name")
        e1.focus_set()

        currentPollutionButton = Button(self, text="Current Pollution Data", command= lambda: self.show_pollution_page(e1.get()), width=20, font=DEFAULTFONT, bg='#B4ADEA')
        currentPollutionButton.place(relx=0.5, rely=0.6, anchor="center")

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
    
    def update_page(self, city_name):

        plt.close('all')
        # This cleans the canvas
        self.canvas.get_tk_widget().pack_forget()
        
        try:
            lat, lon = utils.get_location_coordinates(city_name, self.controller.API_KEY)
            self.cityNameLabel.config(text=city_name.capitalize())

            aqi, components = utils.get_current_pollution_data(lat, lon, self.controller.API_KEY)
            self.aqiLabel.config(text=f'Air Quality Index: {aqi}')

            utils.embed_plot(self, title="Air Quality", city_name=city_name, data=components)

        except:
            self.cityNameLabel.config(text="City not found")
            self.aqiLabel.config(text="Try again")