# MicroPython - Raspberry Pi Pico W
# Brito Guzmán Axel Uriel -19210469
# Código para sensor KY-010 LIGHT BLOCKING

import machine
import time
  
KY010=PIN(7, PIN.IN)

while True:
    if PIN.input(PIN) == 1:
        print("Luz Encendida")
    else:
        print("Luz Apagada")
        time.sleep(1)    