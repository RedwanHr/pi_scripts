import time
import wiringpi

# Define the pins to be used
pin = 3

# Set up the pins
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)

while True:
    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)

    wiringpi.digitalWrite(pin, 1)
    time.sleep(1.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)

    wiringpi.digitalWrite(pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(3)
