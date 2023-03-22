import time
import wiringpi

# Define the pins to be used
pin = 4
input_pin = 2

# Set up the pins
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)
wiringpi.pinMode(input_pin,0)

while True:
    if wiringpi.digitalRead(input_pin) == 0:
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


    