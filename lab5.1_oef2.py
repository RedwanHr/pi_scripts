import time
import wiringpi

# Define the pins to be used
pins = [3, 4, 6]

# Set up the pins
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)

# Flash the LEDs together
while True:
    for pin in pins:
        wiringpi.digitalWrite(pin, 1)
    time.sleep(0.1)
    for pin in pins:
        wiringpi.digitalWrite(pin, 0)
    time.sleep(0.1)