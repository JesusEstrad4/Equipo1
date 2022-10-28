from machine import Pin, ADC
from time import sleep_ms

potX=ADC(26)
potY=ADC(27)

while True:
    valX= potX.read_u16()
    valY= potY.read_u16()
    print("ValX: ", valX, " ValY: ", valY)
    sleep_ms(200)
