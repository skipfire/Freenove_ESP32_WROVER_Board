# https://gist.github.com/projetsdiy/f4330be62589ab9b3da1a4eacc6b6b1c

import machine
from machine import Pin
i2c = machine.I2C(scl=Pin(33), sda=Pin(13))

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
