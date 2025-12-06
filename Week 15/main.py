import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from weather_utils import *

# creates menu screen class
class MenuScreen(Screen):
    pass

# Creates weather screen class
class WeatherScreen(Screen):
    # Simple strings placeholders for the labels on weather screen
    conditions = StringProperty("It is ___")
    temperature = StringProperty("The temperature is ___")
    wind_speed = StringProperty("The wind is traveling ___")
    title = StringProperty("Weather for")

# creates weather screen class
class ErrorScreen(Screen):
    pass

# Runs the actual app
class BitWeatherServicesApp(App):
    # Builds the app, is called when the app.run() is called
    def build(self):
        sm = ScreenManager() # Creates screenmanager object
        Window.bind(on_keyboard=self.on_keyboard) # Binds the keyboard input the self.on_keyboard function

        # Creates three screens for the app based on the classes above and the kivy file
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(WeatherScreen(name='weather'))
        sm.add_widget(ErrorScreen(name='error'))

        # returns a screenmanager so we can switch between screens
        return sm 
    
    def on_keyboard(self, window, keycode, scancode, input_unicode, modifiers):
        # if the enter key is pressed, it will call check_inputs with city and state
        if keycode == 13:
            self.check_inputs(
                city=self.root.get_screen('menu').ids.city_input.text, # get city input text
                state=self.root.get_screen('menu').ids.state_input.text) # get state input text
            return True
        else:
            return False
        
    def check_inputs(self, city, state):
        # cleans up state input
        state = state.strip().upper()
        # gives error screen if city or state is blank
        if not city or not state:
            self.root.current = 'error'
            return
        
        # creates instance of GetWeather class from api_handler
        api_handler = GetWeather(city, state)
        # gets weather data from api
        api_handler.get_weather_data()

        # if the api_handler returned weather data, update the labels on the weather screen
        if api_handler.weather_data:
            weather_screen = self.root.get_screen('weather')
            weather_screen.title = f"Weather For {city}"
            weather_screen.conditions = f"It is {api_handler.conditions}"
            weather_screen.temperature = f"The temperature is {api_handler.temperature}°"
            weather_screen.wind_speed = f"The wind is traveling {api_handler.wind_speed} MPH"

            # change the screen to weather screen
            self.root.current = 'weather'
        else:
            # change the screen to error screen if there was no weather data
            self.root.current = 'error'



# Runs the app if you run the program
if __name__ == '__main__':
    BitWeatherServicesApp().run()