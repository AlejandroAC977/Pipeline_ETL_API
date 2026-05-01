import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_weather(city="Mexico City"):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error de conexion a centro de datos: ", response.status_code)
        return None