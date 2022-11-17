# MicroPython - Raspberry Pi Pico W
# Brito Guzmán Axel Uriel -19210469
# Código para sensor KY-033 TRACKING

from machine import Pin
import utime

sensor = Pin(18, Pin.IN)
utime.sleep(2)

while True:
    if sensor.value() == 1:
        print("Libre")
    else:
        print("Línea")
    utime.sleep(2)