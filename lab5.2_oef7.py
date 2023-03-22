import wiringpi as wp
import time

# set pin numbers
LED_PINS = [3,4,6,9]

# initialize WiringPi
wp.wiringPiSetup()


# set up LED pin as output
for PIN in LED_PINS:
    wp.pinMode(PIN, wp.OUTPUT)

def wavedrive(_ledpins):
    wp.digitalWrite(_ledpins[0], wp.HIGH)
    time.sleep(1)
    wp.digitalWrite(_ledpins[0], wp.LOW)

    wp.digitalWrite(_ledpins[1], wp.HIGH)
    time.sleep(1)
    wp.digitalWrite(_ledpins[1], wp.LOW)

    wp.digitalWrite(_ledpins[2], wp.HIGH)
    time.sleep(1)
    wp.digitalWrite(_ledpins[2], wp.LOW)

    wp.digitalWrite(_ledpins[3], wp.HIGH)
    time.sleep(1)
    wp.digitalWrite(_ledpins[3], wp.LOW)
    
while True:
    wavedrive(LED_PINS)
