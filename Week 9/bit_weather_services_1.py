"""
    Name: bit_weather_services_1.py
    Author: Runtime Rookies
    Created: 10/15/25
    Purpose: Week 9 Milestone 
"""

# Import tkinter library
from tkinter import *

# Import themed widgets (modern styling) from tkinter.ttk
from tkinter.ttk import *

# Define a class to represent the weather app
class WeatherApp():
    # Constructor method that runs when the class is instantiated
    def __init__(self):
        # Set default weather data values
        self.TEMPERATURE = 74 # hard coded constants for now
        self.CONDITIONS = "Sunny"
        self.WIND_SPEED = 8

        # Create the main window for the application
        self.root = Tk()

        # Set the title of the window
        self.root.title("Bit Weather Services")

        # Disable resizing of the window (fixed size)
        self.root.resizable(False, False)

        # Call the method that creates all the GUI widgets
        self.create_widgets()

        # Start the main event loop to keep the window open
        mainloop()

    # Define a method to display weather data when the button is clicked
    def find_weather(self):
        # Update label with stored values
        self.temperature_output.config(text=self.TEMPERATURE, anchor="e") 
        self.conditions_output.config(text=self.CONDITIONS, anchor="e")
        self.wind_speed_output.config(text=self.WIND_SPEED, anchor="e")

    # Define a method to create and position all widgets in the window
    def create_widgets(self):
        # Create a labeled frame to hold weather info
        self.weather_output_frame = LabelFrame(self.root, relief=GROOVE)

        # Create labels for location and weather info
        self.area_name = Label(self.weather_output_frame, text="Weather in Scottsbluff, NE") 
        self.lbl_temperature = Label(self.weather_output_frame, text="Temperature (°F): ")
        self.lbl_conditions = Label(self.weather_output_frame, text="Conditions: ")
        self.lbl_wind_speed = Label(self.weather_output_frame, text="Wind Speed (MPH): ")

        # Create empty labels to display weather data output
        self.temperature_output = Label(self.weather_output_frame, width=10, relief=GROOVE)
        self.conditions_output = Label(self.weather_output_frame, width=10, relief=GROOVE)
        self.wind_speed_output = Label(self.weather_output_frame, width=10, relief=GROOVE)

        # Create a button that triggers the find_weather method
        self.find_weather_btn = Button(self.root, text="Find Weather", command = self.find_weather)

        # Position all static labels (titles) in the grid
        self.area_name.grid(row=0, column=0)
        self.lbl_temperature.grid(row=1, column=0)
        self.lbl_conditions.grid(row=2, column=0)
        self.lbl_wind_speed.grid(row=3, column=0)

        # Position all output labels next to their corresponding text labels
        self.temperature_output.grid(row=1, column=1)
        self.conditions_output.grid(row=2, column=1)
        self.wind_speed_output.grid(row=3, column=1)

        # Place the weather output frame on the main window
        self.weather_output_frame.grid(row=0, column=0)

        # Place the "Find Weather" button below the frame
        self.find_weather_btn.grid(row=1, column=0)

        # Add padding around the frame and button for spacing
        self.weather_output_frame.grid_configure(padx=20, pady=20)
        self.find_weather_btn.grid_configure(padx=20, pady=20)

        # Add internal spacing between all child widgets inside the frame
        for widget in self.weather_output_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

# Create an instance of the WeatherApp class(runs the program)
weather = WeatherApp()