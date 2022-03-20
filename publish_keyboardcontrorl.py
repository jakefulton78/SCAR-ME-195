from os import system
from tarfile import PAX_FIELDS
from time import sleep

from motor_manip import motors
import math

import keyboard
from passwords import mcu_sub

# Global Constants
SCALE = 5
px = 100
py = 100

# Initializations
current_angles= [5,5,5,5]

def increase_px():
    global SCALE, px, py
    px = px + SCALE
    motors(px,py)

def decrease_px():
    global SCALE, px, py
    px = px - SCALE
    motors(px,py)
    
def increase_py():
    global SCALE, px, py
    py = py + SCALE
    motors(px,py)

def decrease_py():
    global SCALE, px, py
    py = py - SCALE
    motors(px,py)

# If increase or decrease key is pressed, a message is sent from the RPi terminal
keyboard.add_hotkey('a', decrease_px)
keyboard.add_hotkey('d', increase_px)
keyboard.add_hotkey('w', increase_py)
keyboard.add_hotkey('s', decrease_py)

# Main Program
if __name__ == "__main__":
    keyboard.wait('esc')
    print("\nExiting program now...\n")