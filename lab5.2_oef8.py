import wiringpi as wp
import time

# set pin numbers
LED_PINS = [3, 4, 6, 9]

# initialize WiringPi
wp.wiringPiSetup()

# set up LED pin as output
for PIN in LED_PINS:
    wp.pinMode(PIN, wp.OUTPUT)

def fullstep(_ledpins, step):
    for i in range(4):
        wp.digitalWrite(_ledpins[i], step[i])

def wavedrive(_ledpins):
    fullstep(_ledpins, [wp.HIGH, wp.LOW, wp.HIGH, wp.LOW])
    time.sleep(1)
    fullstep(_ledpins, [wp.LOW, wp.HIGH, wp.HIGH, wp.LOW])
    time.sleep(1)
    fullstep(_ledpins, [wp.LOW, wp.HIGH, wp.LOW, wp.HIGH])
    time.sleep(1)
    fullstep(_ledpins, [wp.HIGH, wp.LOW, wp.LOW, wp.HIGH])
    time.sleep(1)

while True:
    wavedrive(LED_PINS)
