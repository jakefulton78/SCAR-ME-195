"""
This progam is not the final version of the main program
for the ESP; refer to final_main.py. This program is the 
first program that the MCU would run.
"""

from machine import Pin
import time
import flash_led
import stepper_motor


# Global Constants
DELAY = 1
PIN_RST = 10


# Initializations
pinRST = Pin(PIN_RST, Pin.IN) # This is synthetic for us telling to autohome
print("Running main program.")

# User-defined Functions
def iterate() -> None:
    """This is synthetic code for the motor actuating."""
    stepper_motor.origin += 1

# Interrupts
pinRST.irq(trigger = PIN.IRQ_RISING, handler = stepper_motor.autohome)

# Main Program
while True:
        iterate()
        print(stepper_motor.origin)
        time.sleep(DELAY)

