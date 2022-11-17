# MicroPython - Raspberry Pi Pico W
# Brito Guzmán Axel Uriel -19210469
# Código para sensor KY-034 7 COLOR FLASH

import time
from machine import Pin

led = Pin(26, Pin.OUT)

while True:
    
    print("LED Encendido")
    led.on()  
    time.sleep(3)

    print("LED Apagado")
    led.off()    
    time.sleep(3)