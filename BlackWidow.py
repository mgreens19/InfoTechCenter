# Libraries for system and time manipulation
import sys
import time

# ANSI escape sequences for text colors
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"   # Bold text
GREEN = "\033[32m" # Green text
CYAN = "\033[36m"  # Cyan text
YELLOW = "\033[33m" # Yellow text

# Printing a welcome message in green
print(f"{GREEN}Welcome Branch - Developer: Maddox Greenspoon{RESET}")

# Displaying the name and version of the software system in cyan
print(f"\n\t{CYAN}Welcome to InfoTechCenter V1.0{RESET}")

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
