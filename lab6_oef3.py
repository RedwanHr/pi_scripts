import wiringpi
import time
import json
import requests


url = "http://redwan.hub.ubeac.io/iotessredwan"
uid = "itfactory"

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
        temperature = 100 * 3.3 * tmp0 / 1023
        ActivateADC()
        tmp1 = readadc(1) # read channel 1
        DeactivateADC()
        lux = 100 * (tmp1 - 500) / (1000 - 500)
        print ("Temperature:",round(temperature, 2), "C°","\tLight:",lux,"%")
        data= {
        "id": uid,
        "sensors":[{
            'id': 'adc ch0',
            'data': round(temperature, 2)
             },
             {'id': 'adc ch1',
             'data': lux
            }]
        }

     
        r = requests.post(url, verify=False, json=data)
        print(tmp0, tmp1)
        time.sleep(0.2)
except KeyboardInterrupt:
    DeactivateADC()
    wiringpi.digitalWrite(1, 0) 
    wiringpi.digitalWrite(2, 0) 
    print("\nProgram terminated") 

