import requests
import time

API_KEY = "your_openweathermap_api_key"
CITY = "Delhi"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    print(f"Current temperature in {CITY}: {temp_celsius:.2f}°C")

# Schedule to fetch weather every 5 minutes
while True:
    get_weather()
    time.sleep(300)  # Wait for 5 minutes before fetching again
