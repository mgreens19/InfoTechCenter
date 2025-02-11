import random
from time import sleep

print("\n******************************************\n")
print("Weather Branch - Developer: Maddox Greenspoon")

# Weather Function to determine the weather
def weather():
    """Returns a random weather condition from a predefined list."""
    return random.choice(["snowing", "blizzard", "icy", "rainy", "windy", "sunny"])

# Generate a random weather condition
weatherAlert = weather()

# Mapping weather conditions to alarm delays and speed limits
weather_responses = {
    "snowing": (30, 55),
    "blizzard": (60, 45),
    "icy": (90, 35),
    "rainy": (10, 65),
    "windy": (5, 70),
}

# Function to determine vehicle response based on weather conditions
def vehicleResponseSystem(weatherAlert):
    """Prints an updated alarm time and speed limit based on the current weather condition."""
    if weatherAlert in weather_responses:
        delay, speed = weather_responses[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {delay} minutes because it is {weatherAlert} outside.")
        sleep(1)
        print(f"VRS has been engaged, only allowing us to drive {speed}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weatherAlert} skies outside, drive safe!")
        sleep(1)
        print("VRS has been disengaged, drive safe.")

# Execute the vehicle response system based on the weather condition
vehicleResponseSystem(weatherAlert)
