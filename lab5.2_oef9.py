import wiringpi as wp
import time

# set pin numbers
LED_PINS = [3, 4, 6, 9]
BUTTON_PIN = 2

# initialize WiringPi
wp.wiringPiSetup()

# set up LED pins as output
for PIN in LED_PINS:
    wp.pinMode(PIN, wp.OUTPUT)

# set up button pin as input
wp.pinMode(BUTTON_PIN, wp.INPUT)
wp.pullUpDnControl(BUTTON_PIN, wp.PUD_UP)

# define step sequences for full step mode
FULL_STEP_SEQUENCE = [
    [wp.HIGH, wp.LOW, wp.HIGH, wp.LOW],
    [wp.LOW, wp.HIGH, wp.HIGH, wp.LOW],
    [wp.LOW, wp.HIGH, wp.LOW, wp.HIGH],
    [wp.HIGH, wp.LOW, wp.LOW, wp.HIGH]
]

# define step sequences for half step mode
HALF_STEP_SEQUENCE = [
    [wp.HIGH, wp.LOW, wp.HIGH, wp.LOW],
    [wp.HIGH, wp.LOW, wp.LOW, wp.LOW],
    [wp.HIGH, wp.HIGH, wp.LOW, wp.LOW],
    [wp.LOW, wp.HIGH, wp.LOW, wp.LOW],
    [wp.LOW, wp.HIGH, wp.HIGH, wp.LOW],
    [wp.LOW, wp.LOW, wp.HIGH, wp.LOW],
    [wp.LOW, wp.LOW, wp.HIGH, wp.HIGH],
    [wp.LOW, wp.LOW, wp.LOW, wp.HIGH]
]

def move_stepper(_ledpins, direction, step_sequence):
    if direction == "left":
        step_sequence = list(reversed(step_sequence))
    for step in step_sequence:
        fullstep(_ledpins, step)
        time.sleep(0.01)

def fullstep(_ledpins, step):
    for i in range(4):
        wp.digitalWrite(_ledpins[i], step[i])

# initial direction is right
direction = "right"
# initial mode is full step mode
step_sequence = FULL_STEP_SEQUENCE

while True:
    # read button state
    button_state = wp.digitalRead(BUTTON_PIN)
    if button_state == wp.LOW:
        # change direction
        if direction == "right":
            direction = "left"
        else:
            direction = "right"
        # change step sequence
        if step_sequence == FULL_STEP_SEQUENCE:
            step_sequence = HALF_STEP_SEQUENCE
        else:
            step_sequence = FULL_STEP_SEQUENCE
    # move stepper in current direction and step sequence
    move_stepper(LED_PINS, direction, step_sequence)
