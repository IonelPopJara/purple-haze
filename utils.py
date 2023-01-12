import requests

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def get_location_coordinates(city_name, API_KEY):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}'
    json = requests.get(url).json()

    lat = json[0]['lat']
    lon = json[0]['lon']

    return (lat, lon)

def get_current_pollution_data(lat, lon, API_KEY):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'
    json = requests.get(url).json()

    aqi = json['list'][0]['main']['aqi']
    components = json['list'][0]['components']

    return aqi, components

def embed_plot(self, title, city_name, data):
        pol_components = list(data.keys())
        pol_values = list(data.values())

        plt.style.use('ggplot')

        fig = plt.figure(figsize=(10, 5))

        plt.barh(pol_components, pol_values)

        plt.xlabel('Pollutant Concentration [μg/m3]')
        plt.ylabel('Pollutant')
        plt.title(f'{title} in {city_name}')

        # Embed the graph in the app
        self.canvas = FigureCanvasTkAgg(fig, master = self)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack()