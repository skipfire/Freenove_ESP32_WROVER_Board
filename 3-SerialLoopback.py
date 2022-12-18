from machine import UART, Pin
import time

uart2 = UART(2, baudrate=9600, tx=2, rx=15)
txData = b'hello world'
uart2.write(txData)
time.sleep(0.1)
rxData = bytes()
while uart2.any() > 0:
    rxData += uart2.read(1)

print("Printing received data")
print(rxData.decode('utf-8'))
print("Done printing received data")