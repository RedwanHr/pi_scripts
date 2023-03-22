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
    if switch_state == 0:  # switch is not pressed (power is 1)
        print("LED blinking")
        while True:
            for pin in led_pins:
                wiringpi.digitalWrite(pin, 1)
            time.sleep(0.1)
            for pin in led_pins:
                wiringpi.digitalWrite(pin, 0)
            time.sleep(0.1)
            switch_state = wiringpi.digitalRead(switch_pin)
            if switch_state == 1:  # switch is pressed (power is not 1)
                break
    else:  # switch is pressed (power is not 1)
        print("LED not blinking")
        for pin in led_pins:
            wiringpi.digitalWrite(pin, 0)
        time.sleep(0.1)
