import os
from dotenv import load_dotenv
import requests
from pprint import pprint
import datetime


load_dotenv()
open_weather_token = os.getenv('open_weather_token')


def get_weather(city, weather_token):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
    data = response.json()
    pprint(data)
    city_name = data['name']
    coords = f"Широта: {data['coord']['lat']}, долгота: {data['coord']['lon']}"
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'], )
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    day_duration = sunset - sunrise
    pressure = f"{round(float(data['main']['pressure']) / 1.33)} мм.рт.ст."
    temp = f"{data['main']['temp']} °C"
    feels_temp = f"{data['main']['feels_like']} °C"







def main():
    city = input('Enter the city... ')
    get_weather(city, '16c82c47095d51da5b2db73d2dfbfe8a')


if __name__ == '__main__':
    main()