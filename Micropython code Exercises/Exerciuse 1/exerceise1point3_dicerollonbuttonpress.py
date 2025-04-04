from machine import Pin
import time
import urandom  # Use urandom for random numbers in MicroPython

button = Pin(15, Pin.IN, Pin.PULL_UP)
button_was_pressed = False

while True:
    if button.value() == 0 and not button_was_pressed:
        dice_roll = urandom.getrandbits(3) % 6 + 1  # Random number from 1 to 6
        print("You rolled a", dice_roll)
        button_was_pressed = True
        time.sleep(0.05)  # Debounce delay

    elif button.value() == 1 and button_was_pressed:
        button_was_pressed = False
        time.sleep(0.05)  # Debounce delay
