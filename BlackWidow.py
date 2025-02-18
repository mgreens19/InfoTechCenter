print("\n*********************************************************")
print("Gasoline Branch - Developer: Maddox Greenspoon\n")

import random
from time import sleep


# Function to randomly select a gas level from a predefined list
def gasLevelGauge():
    """Returns a random gas level from the predefined list."""
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to randomly select a nearby gas station from a predefined list
def gasStations():
    """Returns a random gas station name."""
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Bucees"])


# Function to check the gas level and determine the appropriate action
def gasLevelAlert():
    """Checks gas level and provides an alert or recommendation."""

    # Get the current gas level and a random gas station
    gasLevelIndicator = gasLevelGauge()
    gasStation = gasStations()

    # Dictionary to store random distances to gas stations for "Low" and "Quarter Tank" levels
    distances = {
        "Low": round(random.uniform(1, 25), 1),  # Random distance between 1 and 25 miles for "Low"
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
        # Random distance between 25.1 and 50 miles for "Quarter Tank"
    }

    # Dictionary containing messages for each gas level
    messages = {
        "Empty": "*****WARNING - YOU ARE OUT OF GAS.*****\n\nCalling AAA...",
        "Low": f"Your gas tank is extremely low, checking GPS for the closest gas station...\n"
               f"The closest gas station is {gasStation}, which is {distances['Low']} miles away.",
        "Quarter Tank": f"Your gas tank is on a Quarter Tank, checking GPS for the closest gas station...\n"
                        f"The closest gas station is {gasStation}, which is {distances['Quarter Tank']} miles away.",
        "Half Tank": "Your gas tank is on a Half Tank, which is plenty to get to your destination!",
        "Three Quarter Tank": "Your gas tank is Three Quarters full!",
        "Full Tank": "Your gas tank is FULL, Vroom Vroom!"
    }

    # Print the appropriate message based on the gas level
    print(messages[gasLevelIndicator])

    # Add a short delay (1 second) for "Low" and "Quarter Tank" messages to simulate GPS lookup
    sleep(1) if gasLevelIndicator in ["Low", "Quarter Tank"] else None


# Call the function to check gas level and display the appropriate message
gasLevelAlert()