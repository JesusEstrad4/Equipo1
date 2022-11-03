```python
"""
Autor: Dominguez Garcia Jesus Roman
Usuario Github: JesusRomanDG
Fecha: 03 de noviembre de 2022
Descripcion: Haciendo uso del sensor KY-018(PHOTORESISTOR) y un led RGB,
se realiza mediante micropython un programa que enciende led de colores
segun la luz que detecte el sensor.
"""

# importando librerias
from machine import Pin
from machine import ADC
import utime

analogIn = ADC(26) # inicializando el pin 26 como entrada analogica
led = Pin("LED", Pin.OUT) # inicializando el led integrado como salida digital

# inicializando los pines rojo, verde y azul de un led rgb como salidas digitales
red = Pin(2, Pin.OUT)
green = Pin(3, Pin.OUT)

# ciclo
while True:
    
    led.value(1) # enciende el led integrado
    
    lectura = analogIn.read_u16() # guarda el valor de la entrada analogica del fotoresistor
    print(lectura) # imprime el valor obtenido de la lectura
    
    utime.sleep(1) # espera 1 segundo
    
    # si la lectura es mayor a 0 y menor a 10000 entonces enciende el led rojo y apaga el verde y azul
    if lectura>0 and lectura<10000:
        red.value(1)
        green.value(0)
        blue.value(0)
        
    # si la lectura es mayor a 10000 y menor a 20000 entonces enciende el led azul y apaga el rojo y verde
    if lectura>10000 and lectura<20000:
        red.value(0)
        green.value(0)
        blue.value(1)
    
    # si la lectura es mayor a 20000 entonces enciende el led rojo y apaga el verde y azul
    if lectura>20000:
        red.value(0)
        green.value(1)
        blue.value(0)
```
