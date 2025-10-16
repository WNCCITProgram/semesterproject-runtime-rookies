"""
    Name: bit_weather_services_1.py
    Author: Runtime Rookies
    Created: 10/15/25
    Purpose: Week 9 Milestone
"""

from tkinter import *

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
        self.temperature_output.config(text=self.TEMPERATURE, anchor="center")
        self.conditions_output.config(text=self.CONDITIONS, anchor="center")
        self.wind_speed_output.config(text=self.WIND_SPEED, anchor="center")

    def create_widgets(self):
        self.weather_output_frame = LabelFrame(self.root, relief=GROOVE)

        self.area_name = Label(self.weather_output_frame, "Weather in Scottsbluff, NE")
        self.temperature_output = Label(self.weather_output_frame, "")
        self.conditions_output = Label(self.weather_output_frame, "")
        self.wind_speed_output = Label(self.weather_output_frame, "")

        self.find_weather_btn = Button(self.root, "Find Weather", command = self.find_weather)

        self.area_name.grid(row=0, column=0)
        self.temperature_output.grid(row=1, column=0)
        self.conditions_output.grid(row=2, column=0)
        self.wind_speed_output.grid(row=3, column=0)

        self.weather_output_frame.grid(row=0, column=0)
        self.find_weather_btn.grid(row=1, column=0)

        self.weather_output_frame.grid_configure(padx=20, pady=20)
        self.find_weather_btn.grid_configure(padx=20, pady=20)

        for widget in self.weather_output_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)