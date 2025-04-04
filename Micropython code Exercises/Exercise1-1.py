#Exercise 1.1

"""Create a program that blinks the on-board LED to show the SOS sequence in morse code. Each long character
(dah) should last for 1500ms while each short character (dit) should last for 500ms. There should be a 500ms
break between characters and a 1500ms break between letters. After each message, there should be a 3500ms
break and the board should start showing the SOS code again.
"""

from machine import Pin
import time


led = Pin(25, Pin.OUT)  

def blink_dit():
    led.on()
    time.sleep_ms(500)  # dit duration
    led.off()
    time.sleep_ms(500)  # inter-element gap

def blink_dah():
    led.on()
    time.sleep_ms(1500)  # dah duration
    led.off()
    time.sleep_ms(500)   # inter-element gap

def blink_s():
    # S is ··· (three dits)
    blink_dit()
    blink_dit()
    blink_dit()
    # inter-letter gap (already waited 500ms after last dit)
    time.sleep_ms(1500 - 500) 

def blink_o():
    # O is --- (three dahs)
    blink_dah()
    blink_dah()
    blink_dah()
    # inter-letter gap (already waited 500ms after last dah)
    time.sleep_ms(1500 - 500)  

def blink_sos():
    blink_s()
    blink_o()
    blink_s()
    # inter-word gap (already waited 1500ms after last S)
    time.sleep_ms(3500 - 1500)  

while True:
    blink_sos()