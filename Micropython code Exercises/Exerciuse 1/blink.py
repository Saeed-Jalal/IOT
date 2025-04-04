from machine import Pin
import time

# Initialize the LED
led = Pin("LED", Pin.OUT)

# Define Morse code timings
DIT_DURATION = 500        # short blink duration (ms)
DAH_DURATION = 1500       # long blink duration (ms)
CHARACTER_BREAK = 500     # break between blinks (ms)
LETTER_BREAK = 1500       # break between letters (ms)
MESSAGE_BREAK = 3500      # break between repetitions of SOS (ms)

# Function to blink LED for given duration
def blink(duration):
    led.on()
    time.sleep_ms(duration)
    led.off()
    time.sleep_ms(CHARACTER_BREAK)

# Morse code for "S": "..."
def morse_S():
    for _ in range(3):
        blink(DIT_DURATION)

# Morse code for "O": "---"
def morse_O():
    for _ in range(3):
        blink(DAH_DURATION)

# Infinite loop to send SOS in Morse code
while True:
    morse_S()
    time.sleep_ms(LETTER_BREAK)
    morse_O()
    time.sleep_ms(LETTER_BREAK)
    morse_S()
    time.sleep_ms(MESSAGE_BREAK)