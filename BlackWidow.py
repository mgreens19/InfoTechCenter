print("\n******************************************\n")

print("Weather Branch - Developer: Maddox Greenspoon")

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
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 65MPH.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 70MPH.")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")
        sleep(1)
        print("VRS has been disengaged, drive safe.")
# Execute the vehicle response system based on the weather condition
vehicleResponseSystem()
