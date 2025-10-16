"""
    Name: bit_weather_services_1.py
    Author: Runtime Rookies
    Created: 10/15/25
    Purpose: Week 9 Milestone
"""

from tkinter import *
from tkinter.ttk import *

class WeatherApp():

    def __init__(self):
        self.TEMPERATURE = 74
        self.CONDITIONS = "Sunny"
        self.WIND_SPEED = 8

        self.root = Tk()
        self.root.title("Bit Weather Services")

        self.root.resizable(False, False)

        self.create_widgets()
        mainloop()

    def find_weather(self):
        self.temperature_output.config(text=self.TEMPERATURE, anchor="e")
        self.conditions_output.config(text=self.CONDITIONS, anchor="e")
        self.wind_speed_output.config(text=self.WIND_SPEED, anchor="e")

    def create_widgets(self):
        self.weather_output_frame = LabelFrame(self.root, relief=GROOVE)

        self.area_name = Label(self.weather_output_frame, text="Weather in Scottsbluff, NE")
        self.lbl_temperature = Label(self.weather_output_frame, text="Temperature (°F): ")
        self.lbl_conditions = Label(self.weather_output_frame, text="Conditions: ")
        self.lbl_wind_speed = Label(self.weather_output_frame, text="Wind Speed (MPH): ")

        self.temperature_output = Label(self.weather_output_frame, width=10, relief=GROOVE)
        self.conditions_output = Label(self.weather_output_frame, width=10, relief=GROOVE)
        self.wind_speed_output = Label(self.weather_output_frame, width=10, relief=GROOVE)

        self.find_weather_btn = Button(self.root, text="Find Weather", command = self.find_weather)

        self.area_name.grid(row=0, column=0)
        self.lbl_temperature.grid(row=1, column=0)
        self.lbl_conditions.grid(row=2, column=0)
        self.lbl_wind_speed.grid(row=3, column=0)

        self.temperature_output.grid(row=1, column=1)
        self.conditions_output.grid(row=2, column=1)
        self.wind_speed_output.grid(row=3, column=1)

        self.weather_output_frame.grid(row=0, column=0)
        self.find_weather_btn.grid(row=1, column=0)

        self.weather_output_frame.grid_configure(padx=20, pady=20)
        self.find_weather_btn.grid_configure(padx=20, pady=20)

        for widget in self.weather_output_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

weather = WeatherApp()