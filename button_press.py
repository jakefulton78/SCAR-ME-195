from machine import Pin
import flash_led

btn = Pin(9, Pin.IN, Pin.PULL_UP)

if __name__ == "__main__":
    while True:
        print(btn.value())
