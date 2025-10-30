"""
    Name: weather_utils.py
    Author: Noel Onate
    Created: 4/2/25
    Purpose: Store OpenWeatherMap API key and URL for
    easy import into other OpenWeatherMap programs
"""

# OpenWeatherMap API Key
API_KEY = "cbbcc7613091e76023dc824acdd2419c"

# URL to access current weather OpenWeatherMap API
URL = "https://api.openweathermap.org/data/2.5/weather"

import requests, json

class GetWeather():
    def __init__(self, city, state):
        self.city = city
        self.state = state
        self.weather_data = None
    
    def set_location(self, city, state):
        self.city = city
        self.state = state
    
    def get_location(self):
        return f"{self.city}, {self.state}"
    
    def get_weather_data(self):
        try:

            # Build the openweathermap request parameters
            # These are added on to the URL to make the complete request
            query_string = {
                "units": "imperial",        # Units of measure ex: Fahrenheit
                "q": self.get_location(),         # Location for weather
                "appid": API_KEY
            }

            # Get the API JSON data as a Python JSON object
            response = requests.get(
                URL,
                params=query_string
            )
            
            # If the status_code is 200, successful connection and data
            if response.status_code == 200:

                # Get json response into a Python dictionary
                self.weather_data = response.json()

                # Let user know the connection was successful
                print("\n [+] Connection successful.")
            else:
                print(f" Response code: {response.status_code}")
                print(" You may have typed an invalid location.")
                print(" Please try again.")


            # Get weather items from dictionaries
            self.temperature = self.weather_data.get("main").get("temp")
            self.conditions = self.weather_data.get("weather")[0].get("main")
            self.wind_speed = self.weather_data.get("wind").get("speed")

        except:
            # Handle any exceptions
            print("[-] Sorry, there was a problem connecting.")
            self.weather_data = None

