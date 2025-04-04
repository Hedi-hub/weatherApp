import requests

from config import GEO_KEY

GEO_URL = "https://api.api-ninjas.com/v1/geocoding"  # in this website we get all lan and long of every city we want
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherApp:
    def __init__(self, city):
        self.city = city
        self.lat = None
        self.lon = None

    def get_city_co(self):
        headers = {"X-Api-Key": GEO_KEY}
        response = requests.get(f"{GEO_URL}?city={self.city}", headers=headers)

        if response.status_code == 200:
            data = response.json()

            if data:
                self.lat = data[0]["latitude"]
                self.lon = data[0]["longitude"]

            else:
                print("Data not found")

        else:
            print("Not found")

    def get_weather_info(self):
        if self.lat is None or self.lon is None:
            print("Not Found!")

        params = {"latitude": self.lat, "longitude": self.lon, "current_weather": True}

        # API request
        response = requests.get(WEATHER_URL, params=params)  # headers too

        if response.status_code == 200:  # Check if request was successful
            data = response.json()
            current_temp = data["current_weather"]["temperature"]
            current_windspeed = data["current_weather"]["windspeed"]

            # Print weather and clothing suggestion
            print(
                f"The weather in {self.city.capitalize()} is {current_temp}°C with a wind speed of {current_windspeed} km/h.")
            print(suggest_clothing(current_temp))
        else:
            print("Failed to fetch weather data. Please try again later.")


def suggest_clothing(self):
        pass


