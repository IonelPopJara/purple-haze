import config
import requests

def get_location_coordinates(city_name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={config.api_key}'
    json = requests.get(url).json()

    return (json[0]['lat'], json[0]['lon'])

def get_current_pollution_data(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={config.api_key}'
    json = requests.get(url).json()

    aqi = json['list'][0]['main']['aqi']

    return aqi

def get_historical_pollution_data(lat, lon, start, end):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={config.api_key}'
    json = requests.get(url).json()
    total_samples = len(json['list'])
    print(total_samples)

city_name = "berlin"

lat, lon = get_location_coordinates(city_name)

aqi = get_current_pollution_data(lat, lon)

get_historical_pollution_data(lat, lon, 1609455600, 1672527600)

print(f'The current air quality for {city_name} is {aqi}')