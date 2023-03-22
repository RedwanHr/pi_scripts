import time
import wiringpi

# Define the pins to be used
led_pins = [3, 4, 6]
relay_pins = [10, 13, 16, 9]
switch_pin = 2

# Set up the pins
wiringpi.wiringPiSetup()
for pin in relay_pins:
    wiringpi.pinMode(pin, 1)
wiringpi.pinMode(switch_pin, 0)  # set switch pin as input

# Flash the LEDs together
while True:
    # Check the state of the switch
    switch_state = wiringpi.digitalRead(switch_pin)
    if switch_state == 0:  # switch is not pressed (power is 1)
        print("Relays making sound from left to right")
        for pin in relay_pins:
            wiringpi.digitalWrite(pin, 1)
            time.sleep(0.5)
        for pin in reversed(relay_pins):
            wiringpi.digitalWrite(pin, 0)
            time.sleep(0.5)
        switch_state = wiringpi.digitalRead(switch_pin)
        if switch_state == 1:  # switch is pressed (power is not 1)
            continue
    else:  # switch is pressed (power is not 1)
        print("Relays not making sound")
        for pin in relay_pins:
            wiringpi.digitalWrite(pin, 0)
        time.sleep(0.5)
