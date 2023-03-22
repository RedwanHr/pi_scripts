import time
import wiringpi

# Define the pins to be used
led_pins = [3, 4, 6]
switch_pin = 2

# Set up the pins
wiringpi.wiringPiSetup()
for pin in led_pins:
    wiringpi.pinMode(pin, 1)
wiringpi.pinMode(switch_pin, 0)  # set switch pin as input

# Flash the LEDs together
while True:
    # Check the state of the switch
    switch_state = wiringpi.digitalRead(switch_pin)
    if switch_state == 1:  # switch is pressed (power is not 1)
        for pin in led_pins:
            wiringpi.digitalWrite(pin, 0)
    else:  # switch is not pressed (power is 1)
        for pin in led_pins:
            wiringpi.digitalWrite(pin, 1)
        time.sleep(1)
        for pin in led_pins:
            wiringpi.digitalWrite(pin, 0)
        time.sleep(1)

