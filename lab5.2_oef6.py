import time
import wiringpi

led_pins = [3, 4, 6]
relay_pins = [10, 13, 16, 9]
gpio1_pin = 1
gpio2_pin = 2

wiringpi.wiringPiSetup()
for pin in relay_pins:
    wiringpi.pinMode(pin, 1)
    wiringpi.pinMode(gpio1_pin, 0) # set gpio1 pin as input
    wiringpi.pinMode(gpio2_pin, 0) # set gpio2 pin as input

while True:
    gpio2_state = wiringpi.digitalRead(gpio2_pin)
    gpio1_state = wiringpi.digitalRead(gpio1_pin)

    if gpio2_state == 1:  # GPIO2 is activated
        print("Switching the first relay")
        wiringpi.digitalWrite(relay_pins[0], 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(relay_pins[0], 0)
        time.sleep(0.5)
    elif gpio1_state == 1:  # GPIO1 is activated
        print("Switching the second relay")
        wiringpi.digitalWrite(relay_pins[1], 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(relay_pins[1], 0)
        time.sleep(0.5)

