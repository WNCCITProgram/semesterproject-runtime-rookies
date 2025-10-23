"""
    Name: weather_1.py
    Author: Noel Onate
    Created: 4/13/25
    Purpose: Display Openweathermap weather from user input
"""

# pip install requests
import requests
# Import Openweather map api key and URL
import weather_utils
# pip install rich
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()


class Weather:
    def __init__(self):
        console.print(
            Panel.fit(
                "  --  Noel's OpenWeatherMap App  --  ",
                style="bold green",
                subtitle="By Noel Onate",
            )
        )

    def get_location(self):
        """Get location from user."""
        self.city = input("Enter city: ")
        self.state = input("Enter state: ")
        self.country = input("Enter country: ")

        # Build the weather query
        self.location = f"{self.city}, {self.state}, {self.country}"
    
    def get_weather(self):
        """Get weather data from Openweathermap"""
        try:
            # Build the openweathermap request parameters
            # These are added on to the URL to make the complete request
            query_string = {
                "units": "imperial",        # Units of measure ex: Fahrenheit
                "q": self.location,         # Location for weather
                "appid": weather_utils.API_KEY
            }

            # Get the API JSON data as a Python JSON object
            response = requests.get(
                weather_utils.URL,
                params=query_string
            )

            # If the status_code is 200, successful connection and data
            if response.status_code == 200:

                # Get json response into a Python dictionary
                self.weather_data = response.json()

                # Let user know the connecction was successful
                print("\n [+] Connection successful.")
            else:
                print(f" Response code: {response.status_code}")
                print(" You may have typed an invalid location.")
                print(" Please try again.")
                self.get_location()


            # Get weather items from dictionaries
            self.description = self.weather_data.get(
                "weather")[0].get("description").title()
            self.temperature = self.weather_data.get("main").get("temp")
            self.humidity = self.weather_data.get("main").get("humidity")
        
        except:
            # Handle any exceptions
            print("[-] Sorry, there was a problem connecting.")

    def display_weather(self):
        # Display current weather
        print(f"\n Current weather in {self.city.title()}")
        print(f" Description: {self.description}")
        print(f" Temperature: {self.temperature:.1f}°F")
        print(f" Humidity:    {self.humidity} %")

"""The main program starts here. Create a Weather program object"""
weather = Weather()
weather.get_location()
weather.get_weather()
weather.display_weather()
