import kivy
kivy.require('1.0.5')
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from weather_utils import *
# defines functions and layout
class MenuScreen(Screen):
    pass

class WeatherScreen(Screen):
    conditions = StringProperty("It is ___")
    temperature = StringProperty("The temperature is ___")
    wind_speed = StringProperty("The wind is traveling ___")
    title = StringProperty("Weather for")

class ErrorScreen(Screen):
    pass

# Runs the actual app
class BitWeatherServicesApp(App):
    def build(self):
        sm = ScreenManager()
        Window.bind(on_keyboard=self.on_keyboard)
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(WeatherScreen(name='weather'))
        sm.add_widget(ErrorScreen(name='error'))
        return sm
    def on_keyboard(self, window, keycode, scancode, input_unicode, modifiers):
        if keycode == 13:
            self.check_inputs()
            print("Enter!")
            return True
        else:
            return False
    def check_inputs(self, city, state):
        state = state.strip().upper()
        if not city or not state:
            self.root.current = 'error'
            return
        
        api_handler = GetWeather(city, state)
        api_handler.get_weather_data()

        if api_handler.weather_data:
            weather_screen = self.root.get_screen('weather')
            weather_screen.title = f"Weather For {city}"
            weather_screen.conditions = f"It is {api_handler.conditions}"
            weather_screen.temperature = f"The temperature is {api_handler.temperature}°"
            weather_screen.wind_speed = f"The wind is traveling {api_handler.wind_speed} MPH"
            self.root.current = 'weather'
        else:
            self.root.current = 'weather'



if __name__ == '__main__':
    BitWeatherServicesApp().run()