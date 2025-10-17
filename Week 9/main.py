"""
    Name: bit_weather_services_1.py
    Author: Runtime Rookies
    Created: 10/15/25
    Purpose: Week 9 Milestone
"""
from tkinter import *
from tkinter import ttk


class Bit_Weather_Services(Tk):
    def __init__(self):
        # initializes
        super().__init__() # calls __init__ function of the TK (parent) class
        self.title("Bit Weather Services") # Sets window title
        self.geometry("620x400") # sets window size
        self.resizable(False, False) # makes wind not resizable

        # Weather info
        # These hold the text that will be displayed in the weather results
        self.conditions_text = StringVar(value="It is ____") # text for weather conditions
        self.temperature_text = StringVar(value="The temperature is ___") # text for temperature
        self.wind_speed_text = StringVar(value="The wind is traveling ____") # text for wind speed

        # Variables
        # These will change depending on what the user puts in the entry fields
        self.state = StringVar() # variable for state
        self.city = StringVar() # variable for city
        # will change depending on what the api returns
        self.conditions = StringVar() # variable for weather conditions
        self.temperature = StringVar() # variable for temperature
        self.wind_speed = StringVar() # variable for wind speed

        # Labels
        # These honestly don't need to be StringVars, but they are for future proofing
        self.state_text = StringVar(value="Enter State Name: ") # text for state label
        self.city_text = StringVar(value="Enter City Name: ") # text for city label
        self.weather_title_text = StringVar(value="Weather for") # text for title in weather frame

        # Frames
        self.wf = Frame(self, width=600, height=400, bg="grey") # (weather frame) frame to display weather results
        self.mf = Frame(self, width=600, height=400, bg="grey") # (main frame) frame to display main menu
        
    def display_weather(self):
        self.mf.pack_forget() # unpacks main frame
        self.wf.pack(fill="both", expand=True) # packs weather frame

    def display_menu(self):
        self.wf.pack_forget() # unpacks weather frame
        self.mf.pack(fill="both", expand=True) # packs main frame

    def check_inputs(self):
        # Read Entries and store them as temporary variables
        state = self.state.get() # stores text in state entry
        city = self.city.get() # stores text in city entry
        
        # temporarily hardcoded to true till we add the api #TODO: add api (:
        inputs_valid = True

        # Title is the only value of all of the results we can update before adding the api
        self.weather_title_text.set(f"Weather For {self.city.get()}") # updates value of the title to include the city

        # if there is text in both city and state entries and input is 
        # valid for the api it calls the class display_weather method
        if city and state:
            if inputs_valid:
                self.display_weather() # displays weather results

    def pack_frames(self):
        ### MENU FRAME
        # images
        self.title_img = PhotoImage(file="semesterproject-runtime-rookies/title_image.png") # grabs image for the title in menu
        self.cloud_img = PhotoImage(file="semesterproject-runtime-rookies/cloud.png") # grabs image for the button to get weather

        # Widgets
        self.menu_title = ttk.Label(self.mf, image=self.title_img, width=600) # label showing title
        self.state_label = ttk.Label(self.mf, textvariable=self.state_text, font=("Brush Script MT", 24), background="grey") # label for state
        self.city_label = ttk.Label(self.mf, textvariable=self.city_text, font=("Brush Script MT", 24), background="grey") # label for city
        self.state_input = ttk.Entry(self.mf, textvariable=self.state) # entry for state
        self.city_input = ttk.Entry(self.mf, textvariable=self.city) # entry for city
        self.get_weather_button = ttk.Button(self.mf, command=self.check_inputs, image=self.cloud_img) # button with cloud image to get weather
        # Packing
        self.menu_title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=8, pady=5) # packs title
        self.state_label.grid(row=1, column=0, sticky="s", padx=20, pady=(20, 0)) # packs state label
        self.state_input.grid(row=2, column=0, sticky="ew", padx=20) # packs state entry
        self.city_label.grid(row=1, column=1, sticky="s", padx=20, pady=(20, 0)) # packs city label
        self.city_input.grid(row=2, column=1, sticky="ew", padx=20) # packs city entry
        self.get_weather_button.grid(row=3, column=0, columnspan=2, pady=30, ipadx=5, ipady=5) # packs button to check weather
        # Configuring
        self.mf.columnconfigure(0, weight=1) # ensures both colums expand equally
        self.mf.columnconfigure(1, weight=1) # they keep the text for the input labels nice


        ### WEATHER FRAME
        # Widgets
        self.weather_title = ttk.Label(self.wf, textvariable=self.weather_title_text, font=("Arial", 24)) # label for title
        self.conditions_label = ttk.Label(self.wf, textvariable=self.conditions_text, font=("Arial", 18), background="grey") # label for conditions
        self.temperature_label = ttk.Label(self.wf, textvariable=self.temperature_text, font=("Arial", 18), background="grey") # label for temperature
        self.wind_speed_label = ttk.Label(self.wf, textvariable=self.wind_speed_text, font=("Arial", 18), background="grey") # label for wind speed
        self.return_to_menu_button = ttk.Button(self.wf, text="Back", command=self.display_menu) # Button to return to the main menu
        # Packing
        self.return_to_menu_button.grid(row=0, column=0, padx=5, pady=5, sticky="nw") # packs button to return
        self.weather_title.grid(row=0, column=1, pady=20) # packs title label
        self.conditions_label.grid(row=1, column=1, pady=10) # packs conditions label
        self.temperature_label.grid(row=2, column=1, pady=10) # packs temperature label
        self.wind_speed_label.grid(row=3, column=1, pady=10) # packs wind speed label



if __name__ == "__main__":
    weather = Bit_Weather_Services() # creats instance of class
    weather.pack_frames() # packs frames (for the main and weather windows)
    weather.display_menu() # display menu frame
    weather.mainloop() # starts tkinters loop so it works