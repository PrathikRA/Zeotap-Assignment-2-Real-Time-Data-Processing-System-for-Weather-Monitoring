import requests
import time
from runtest import OPENWEATHER_API_KEY, CITIES, POLL_INTERVAL

class WeatherDataProcessor:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY

    def get_weather_data(self, city):
        """
        Fetching weatherdata from OpenWeatherMap API.
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return {
            "city": city,
            "main": data['weather'][0]['main'],
            "temp": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "dt": data['dt']
        }

    def convert_temp(self, kelvin, unit="celsius"):
        """
        Converting temperature from Kelvin to Celsius or Fahrenheit.
        """
        if unit == "celsius":
            return kelvin - 273.15
        elif unit == "fahrenheit":
            return (kelvin - 273.15) * 9/5 + 32
        else:
            raise ValueError("Unsupported temperature unit")

    def process_data(self):
        """
        fetch and process weather data for all the cities.
        """
        while True:
            weather_data = []
            for city in CITIES:
                data = self.get_weather_data(city)
                data['temp_c'] = self.convert_temp(data['temp'], "celsius")
                data['feels_like_c'] = self.convert_temp(data['feels_like'], "celsius")
                weather_data.append(data)

            print(weather_data)

            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    processor = WeatherDataProcessor()
    processor.process_data()
