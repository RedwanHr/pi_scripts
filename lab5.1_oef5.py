import time
import wiringpi

# Define the pins to be used
pins = [3, 4, 6]

# Set up the pins
wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)

# Turn on LED1 and LED3 together, and then LED2 and LED4 together, with a 1-second interval
while True:
    # Turn on LED1 and LED3
    wiringpi.digitalWrite(3, 1)
    wiringpi.digitalWrite(4, 1)
    time.sleep(1)
    # Turn off LED1 and LED3
    wiringpi.digitalWrite(3, 0)
    wiringpi.digitalWrite(4, 0)

    # Turn on LED2 and LED4
    wiringpi.digitalWrite(4, 1)
    wiringpi.digitalWrite(6, 1)
    time.sleep(1)
    # Turn off LED2 and LED4
    wiringpi.digitalWrite(4, 0)
    wiringpi.digitalWrite(6, 0)
