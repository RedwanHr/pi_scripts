import wiringpi
import time

# GPIO pins that will connect HC-SR04 to the Orange Pi PCB
TRIG = 0
ECHO = 1

wiringpi.wiringPiSetup()

while True:
    wiringpi.pinMode(TRIG, wiringpi.OUTPUT)
    wiringpi.pinMode(ECHO, wiringpi.INPUT)

    wiringpi.digitalWrite(TRIG, wiringpi.LOW)

    time.sleep(0.5)
    wiringpi.digitalWrite(TRIG, wiringpi.HIGH)
    time.sleep(0.00001)
    wiringpi.digitalWrite(TRIG, wiringpi.LOW)

    while wiringpi.digitalRead(ECHO) == wiringpi.LOW:
        pulse_start = time.time()

    while wiringpi.digitalRead(ECHO) == wiringpi.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance: " + str(distance) + "cm")
    
    time.sleep(0.1)
