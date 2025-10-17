"""
    Name: main.py
    Author: Runtime Rookies
    Created: 10/15/25
    Purpose: Week 9 Milestone
"""

from tkinter import *
from tkinter import ttk

class WeatherApp(Tk):

    def __init__(self):
        # initializes
        super().__init__()
        self.title("Bit Weather Services")
        self.geometry("600x400")
        self.resizable(False, False)

        # Inputs
        self.state = StringVar()
        self.city = StringVar()

        # Labels
        self.title_text = StringVar(value="Bit Weather Services")
        self.state_text = StringVar(value="Enter State Name: ")
        self.city_text = StringVar(value="Enter City Name: ")
        self.button_text = StringVar(value="Get Weather")

    def check_inputs(self):
        # Grabs the values from the entry boxes
        state = self.state.get()
        city = self.city.get()

        inputs_valid = True

        # Talks to the other class
        if state and city:
            if inputs_valid:
                self.display_weather()
        
    def display_weather(self):
        # wf (WEATHER FRAME) for showing weather
        self.wf = ttk.Frame(self, width=600,height=400)

    #def find_weather(self):
    #    self.temperature_output.config(text=self.TEMPERATURE, anchor="e")
    #    self.conditions_output.config(text=self.CONDITIONS, anchor="e")
    #    self.wind_speed_output.config(text=self.WIND_SPEED, anchor="e")

    def display_menu(self):
        # mf (MENU FRAME) for asking user to input data
        self.mf = Frame(self, width=600, height=400, bg="lightgray")

        # tf stands for title frame
        self.tf = Frame(self.mf, width=600, height=200, bg="lightgray")

        # Image
        self.logo_img = PhotoImage(file="dnalogo.png")
        # Top area
        self.left_img = ttk.Label(self.tf, image=self.logo_img, width=40) # left image
        self.right_img = ttk.Label(self.tf, image=self.logo_img) # right image
        self.title_label = ttk.Label(self.tf, textvariable=self.title_text, 
                                     background="lightgray", font="helpmepickafont 24", 
                                     ) # title in the midle
        self.seperator = ttk.Separator(self.mf, orient="horizontal", style="Horizontal.TSeparator") # seperator bar underneath

        # input labels
        self.state_label = ttk.Label(self.mf, textvariable=self.state_text) # label asking for state name
        self.city_label = ttk.Label(self.mf, textvariable=self.city_text) # label asking for city name
        # input entries
        self.state_input = ttk.Entry(self.mf, textvariable=self.state) # entry for state
        self.city_input = ttk.Entry(self.mf, textvariable=self.city) # entry for city

        # go button
        self.get_weather_button = ttk.Button(self.mf, text=self.button_text, command=self.check_inputs)

        # places iamges and title on the grid and seperator
        self.left_img.grid(row=0, column=0, padx=40, pady=8, sticky="w")
        self.title_label.grid(row=0, column=1, padx=8, pady=8)
        self.right_img.grid(row=0, column=2, padx=40, pady=8, sticky="e")

        # places title box and 
        self.tf.grid(row=0, column=1)
        self.tf.columnconfigure(0, weight=0)
        self.tf.columnconfigure(1, weight=1)
        self.tf.columnconfigure(2, weight=0)

        self.seperator.grid(row=1, column=1, columnspan=3, sticky="n")


        self.mf.pack(fill="both", expand=True)

    



if __name__ == "__main__":
    weather = WeatherApp()
    weather.display_menu()
    weather.mainloop()