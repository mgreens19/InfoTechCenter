# Libraries for system and time manipulation
import sys
import time
import random
from time import sleep

# ANSI escape sequences for text colors
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"   # Bold text
GREEN = "\033[32m" # Green text
CYAN = "\033[36m"  # Cyan text
YELLOW = "\033[33m" # Yellow text

# Printing a welcome message in green
print(f"{GREEN}Welcome Branch - Developer: Maddox Greenspoon{RESET}\n")

# Displaying the name and version of the software system in cyan
print(f"{CYAN}Welcome to InfoTechCenter V1.0{RESET}\n")

# Initialize counters for progress and ellipsis
x = 0
ellipsis = 0

# Loop that simulates the system booting up with animated ellipsis
while x != 20:
    x += 1  # Increment the iteration counter
    
    # Creating the boot message with an increasing number of dots (ellipsis) in yellow
    message = f"{YELLOW}Infotech Center System Booting{RESET}" + "." * ellipsis
    
    ellipsis += 1  # Increase the number of dots for the next iteration
    
    # Write the message to the console, overwriting the previous line
    sys.stdout.write("\r" + message)
    
    # Pause for 0.5 seconds to simulate loading time
    time.sleep(.5)
    
    # Reset ellipsis back to 0 after it reaches 4 dots
    if ellipsis == 4:
        ellipsis = 0
    
    # Check if 20 iterations have passed (end of the booting sequence)
    if x == 20:
        # Print a final message in bold green, indicating system boot-up completion
        print(f"\n\n{BOLD}{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}\n")


print("\n*********************************************************")
print("Gasoline Branch - Developer: Maddox Greenspoon\n")

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

