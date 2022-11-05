"""
Omar Gamaliel Rodriguez Moreno
Usuario Barny-Claus
Estudiante del Instituto Tecnológico de Tijuana
  Materia: Sistemas programables
"""
from machine import Pin
import time,utime  

iman=Pin(15,Pin.IN)  
led=Pin(16,Pin.OUT)  
while True:
    try:
        if iman.value() == 0:
            led.value(0)
        elif iman.value()==1:
            led.value(1)
    except KeyboardInterrupt:
        break
