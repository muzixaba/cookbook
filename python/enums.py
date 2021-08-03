from enum import Enum

# Enums are used to represent a class of constant values
class TrafficLight(Enum):
    GREEN = 1
    AMBER = 2
    RED = 3


red = TrafficLight.Red

print(red)