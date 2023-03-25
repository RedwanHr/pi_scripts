import wiringpi
import time

def ActivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 0) # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1) # Deactived ADC using CS
    time.sleep(0.000005)

def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    return adcout

#Setup
pin_CS_adc = 16 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1) # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0) #(channel, port, speed, mode)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)


try:
    while True:
        ActivateADC()
        tmp0 = readadc(0) # read channel 0
        DeactivateADC()
        ActivateADC()
        tmp1 = readadc(1) # read channel 1
        DeactivateADC()
        print ("input0:",tmp0,"input1:",tmp1)
        
        # check if tmp0 is greater than tmp1
        if tmp0 > 1.1 * tmp1:
            # turn on LED A and turn off LED B
            wiringpi.digitalWrite(1, 1) # turn on LED A
            wiringpi.digitalWrite(2, 0) # turn off LED B
        elif tmp1 > 1.1 * tmp0:
            # turn off LED A and turn on LED B
            wiringpi.digitalWrite(1, 0) # turn off LED A
            wiringpi.digitalWrite(2, 1) # turn on LED B
            
        time.sleep(0.2)
except KeyboardInterrupt:
    DeactivateADC()
    # turn off both LEDs before exiting the program
    wiringpi.digitalWrite(1, 0) # turn off LED A
    wiringpi.digitalWrite(2, 0) # turn off LED B
    print("\nProgram terminated") 
