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
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
GEOMAP_URL = "http://api.openweathermap.org/geo/1.0/direct"

# List of state abreviations for input
STATES = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
           'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
             'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
               'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')
# Imports for API use
import requests, json
# Class for utils
class GetWeather():
    def __init__(self, city, state):
        self.set_location(city, state)
        self.latitude = None
        self.longitude = None
        self.weather_data = None
    # Set location based on user input
    def set_location(self, city, state):
        if state.upper() in STATES:
            self.state = state
        self.city = city
    # Get coordinates base on the location the user inputted
    def get_coordinates(self):
        try:
            query_string = {
                "q": self.get_location(),        # Location for weather
                "limit": 5,
                "appid": "295ba02a2d7c1e90d464ea247bfad517"
            }

            response = requests.get(
                GEOMAP_URL,
                params=query_string
            )

            if response.status_code == 200:
                self.location_data = response.json()[0]
                self.latitude = self.location_data["lat"]
                self.longitude = self.location_data["lon"]
                print(f"[+] Coordinates found: {self.latitude}, {self.longitude}")
            else:
                print(f" Response code: {response.status_code}")
                print(" You may have typed an invalid location.")
                print(" Please try again.")

            # Update latitude and longitude
        
        except:
            print("[-] Sorry, there was a problem connecting")
    # get the location from set_location function
    def get_location(self):
        return f"{self.city}, {self.state}, US"
    # Get weather stuff from API
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
                WEATHER_URL,
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

if __name__ == "__main__":
    test = GetWeather("NE", "Scottsbluff")
    test.get_coordinates()
    print(test.latitude, test.longitude)
