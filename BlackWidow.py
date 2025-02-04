# Libraries for system and time manipulation
import sys
import time

# Printing a welcome message to the console
print("Welcome Branch - Developer: Maddox Greenspoon")

# Displaying the name and version of the software system
print("\n\tWelcome to InfoTechCenter V1.0")

# Initialize counters for progress and ellipsis
x = 0
ellipsis = 0

# Loop that simulates the system booting up with animated ellipsis
while x != 20:
    x += 1  # Increment the iteration counter
    # Creating the boot message with an increasing number of dots (ellipsis)
    message = ("Infotech Center System Booting" + "." * ellipsis)
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
        # Print a message indicating the system has fully booted
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")
