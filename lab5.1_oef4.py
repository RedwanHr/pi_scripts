import time
import wiringpi

# Define the pins to be used
pins = [3, 4, 6]

# Set up the pins
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)

# Run the light in both directions
while True:
    # Move from left to right
    for i in range(len(pins)):
        wiringpi.digitalWrite(pins[i], 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(pins[i], 0)

    # Move from right to left
    for i in range(len(pins) -1):
        wiringpi.digitalWrite(pins[i], 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(pins[i], 0)
