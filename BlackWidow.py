print("\n******************************************\n")

print("Weather Branch - Developer: Maddox Greenspoon\n")

# Import necessary libraries for random weather generation and timing
import random
from time import sleep

# Weather Function to determine the weather
def weather():
    """Returns a random weather condition from a predefined list."""
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

# Generate a random weather condition
weatherAlert = weather()

# Function to determine vehicle response based on weather conditions
def vehicleResponseSystem():
    """Prints an updated alarm time based on the current weather condition."""
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is", weatherAlert, "outside.")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")

# Execute the vehicle response system based on the weather condition
vehicleResponseSystem()
