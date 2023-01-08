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
    components = {'co': 0, 'no': 0, 'no2': 0, 'o3': 0, 'so2': 0, 'pm2_5': 0, 'pm10': 0, 'nh3': 0}

    average_co = 0
    average_no = 0
    average_no2 = 0
    average_o3 = 0
    average_so2 = 0
    average_nh3 = 0
    average_pm10 = 0
    average_pm2_5 = 0
    for item in json['list']:
        average_aqi += item['main']['aqi']
        average_co += item['components']['co']
        average_no += item['components']['no']
        average_no2 += item['components']['no2']
        average_o3 += item['components']['o3']
        average_so2 += item['components']['so2']
        average_nh3 += item['components']['nh3']
        average_pm10 += item['components']['pm10']
        average_pm2_5 += item['components']['pm2_5']
    
    average_aqi /= total_samples
    average_co /= total_samples
    average_no /= total_samples
    average_no2 /= total_samples
    average_o3 /= total_samples
    average_so2 /= total_samples
    average_nh3 /= total_samples
    average_pm10 /= total_samples
    average_pm2_5 /= total_samples

    components = {'co': average_co, 'no': average_no, 'no2': average_no2, 'o3': average_o3, 'so2': average_so2, 'pm2_5': average_pm2_5, 'pm10': average_pm10, 'nh3': average_nh3}

    # Maybe turn this function into a utils function
    components_rounded = dict()
    for key in components:
        components_rounded[key] = round(components[key], 2)

    return average_aqi, components_rounded

city_name = "copiapo"

lat, lon = get_location_coordinates(city_name)

aqi, components = get_current_pollution_data(lat, lon)

avg_aqi, avg_components = get_historical_pollution_data(lat, lon, 1669849200, 1669885200)

print(f'The current air quality for {city_name} is {aqi}')
print(f'\tThe components are: {components}\n')
print(f'The average air quality for {city_name} is {avg_aqi}')
print(f'\tThe average components are: {avg_components}\n')
