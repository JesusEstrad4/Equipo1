```python
"""
Autor: Dominguez Garcia Jesus Roman
Usuario Github: JesusRomanDG
Fecha: 03 de noviembre de 2022
Descripcion: Haciendo uso del sensor KY-016(RGB LED), se realiza
mediante micropython un programa que enciende los distintos leds
incluidos en el componente.
"""

# importando librerias
from machine import Pin
import utime

# inicializando los pines rojo, verde y azul de un led rgb como salidas digitales
red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
blue = Pin(20, Pin.OUT)

# ciclo
while True:
    
    # enciende y apaga led rojo
    red.value(1)
    utime.sleep(1)
    red.value(0)
    utime.sleep(1)
    
    # enciende y apaga el led verde
    green.value(1)
    utime.sleep(1)
    green.value(0)
    utime.sleep(1)
    
    # enciende y apaga el led azul
    blue.value(1)
    utime.sleep(1)
    blue.value(0)
    utime.sleep(1)
    
    # enciende y apaga los leds rojo y azul
    red.value(1)
    blue.value(1)
    utime.sleep(1)
    red.value(0)
    blue.value(0)
    utime.sleep(1)
    
    # enciende y apaga los leds verde y azul
    green.value(1)
    blue.value(1)
    utime.sleep(1)
    green.value(0)
    blue.value(0)
    utime.sleep(1)
    
    # enciende y apaga los leds rojo y verde
    green.value(1)
    red.value(1)
    utime.sleep(1)
    green.value(0)
    red.value(0)
    utime.sleep(1)
```