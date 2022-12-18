from machine import Pin
import ds18b20
from ds18b20 import ds

red=32
green=33
blue=4
btn=12
w1=14
fnBtn = Pin(btn, mode=Pin.IN, pull=Pin.PULL_UP)
redLed = Pin(red, mode=Pin.OUT)
greenLed = Pin(green, mode=Pin.OUT)
blueLed = Pin(blue, mode=Pin.OUT)
sensor=ds(w1,'f',12) #creates sensor object set to default pin 2, units in Celcius, resolution 12 bit
ledOn = False
counter = 0
while counter < 10:
    ledOn = not ledOn
    redLed.value(ledOn)
    greenLed.value(ledOn)
    blueLed.value(ledOn)
    counter += 1
    temp=ds18b20.read(sensor) # a time.sleep is builtin to the function to allow time to take the reading
    print (temp)
    print(fnBtn.value())
    time.sleep(0.5)
print("Done")


