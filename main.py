import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_location_coordinates(city_name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}'
    json = requests.get(url).json()

    return (json[0]['lat'], json[0]['lon'])

def get_current_pollution_data(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'
    json = requests.get(url).json()

    aqi = json['list'][0]['main']['aqi']
    components = json['list'][0]['components']

    return aqi, components

def get_historical_pollution_data(lat, lon, start, end):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_KEY}'
    json = requests.get(url).json()

    total_samples = len(json['list'])

    average_aqi = 0

    avg_components = {'co': 0, 'no': 0, 'no2': 0, 'o3': 0, 'so2': 0, 'pm2_5': 0, 'pm10': 0, 'nh3': 0}

    for item in json['list']:
        average_aqi += item['main']['aqi']

        for key in avg_components:
            avg_components[key] += item['components'][key]
    
    average_aqi /= total_samples

    # Maybe turn this function into a utils function
    components_rounded = dict()
    for key in avg_components:
        avg_components[key] = avg_components[key] / total_samples
        components_rounded[key] = round(avg_components[key], 2)

    return average_aqi, components_rounded

city_name = "copiapo"

lat, lon = get_location_coordinates(city_name)

aqi, components = get_current_pollution_data(lat, lon)

avg_aqi, avg_components = get_historical_pollution_data(lat, lon, 1669849200, 1669885200)

import matplotlib.pyplot as plt

data = components

pol_components = list(data.keys())
pol_values = list(data.values())

plt.style.use('ggplot')

plt.barh(pol_components, pol_values,)

plt.title(f'Air Quality in {city_name.capitalize()}')
plt.xlabel('Pollutant Concentration [μg/m3]')
plt.ylabel('Pollutant')
plt.show()
