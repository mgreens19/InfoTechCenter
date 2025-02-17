print("\n*********************************************************")
print("Gasoline Branch - Developer: Maddox Greenspoon\n")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
  return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Bucees"]
    return random.choice(gasStationsList)

def gasLevelAlert():
 milesToGasStationLow = round(random.uniform(1,25),1)
 milesToGasStationQuarterTank = round(random.uniform(25.1, 50),1)
 gasLevelIndicator = gasLevelGauge()
 if gasLevelIndicator == "Empty":
    print("*****WARNING - YOU ARE OUT OF GAS*****\n")
    sleep(1)
    print("Calling AAA")
 elif gasLevelIndicator == "Low":
   print("Your gas tank is extremely low, checking GPS for the closest gas station")
   sleep(1)
   print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
 elif gasLevelIndicator == "Quarter Tank":
   print("Your gas tank is on a Quarter Tank, checking GPS for the closest gas station")
   sleep(1)
   print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
 elif gasLevelIndicator == "Half Tank":
   print("Your gas tank is on a Half Tank, which is plenty to get to your destination!")
 elif gasLevelIndicator == "Three Quarter Tank":
   print("Your gas tank is Three Quarters of a Tank full!")
 else:
     print("Your gas tank is FULL, Vroom Vroom!")
  gasLevelAlert()
