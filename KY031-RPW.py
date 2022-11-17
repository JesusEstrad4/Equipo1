# MicroPython - Raspberry Pi Pico W
# Brito Guzmán Axel Uriel -19210469
# Código para sensor KY-031 TAP MODULE

import time
from machine import Pin

pico_led = Pin(25, Pin.OUT)
knock = Pin(16, Pin.IN)

while True:
    if(knock.value() == 1):
        pico_led.value(1)
        time.sleep(2)
    else:
        pico_led.value(0)
        time.sleep(2)