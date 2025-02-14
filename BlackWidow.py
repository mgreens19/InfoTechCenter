print("\n*********************************************************")
print("Gasoline Branch - Developer: Maddox Greenspoon\n")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
  return random.choice(gasLevelList)

print(gasLevelGauge())