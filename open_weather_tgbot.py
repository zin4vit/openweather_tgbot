import requests
import datetime
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


load_dotenv()

bot_token = os.getenv('bot_token')
open_weather_token = os.getenv('open_weather_token')


bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer('Привет! Это погодный бот. Введи название города.')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
        data = response.json()
        city_name = data['name']
        coords = f"Широта: {data['coord']['lat']}, долгота: {data['coord']['lon']}"
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'], )
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        day_duration = sunset - sunrise
        pressure = f"{round(float(data['main']['pressure']) / 1.33)} мм.рт.ст."
        temp = f"{data['main']['temp']} °C"
        feels_temp = f"{data['main']['feels_like']} °C"
        await message.answer(f"*** {city_name} ***\n"
                             f"{coords}\n"
                             f"Восход: {sunrise}\n"
                             f"Закат: {sunset}\n"
                             f"Продолжительность дня: {day_duration}\n"
                             f"Атмосферное давление: {pressure}\n"
                             f"Температура: {temp}\n"
                             f"Ощущается как: {feels_temp}\n")

    except:
        await message.answer('Что-то пошло не так. Проверь название города.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)