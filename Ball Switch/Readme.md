```python
"""
Autor: Dominguez Garcia Jesus Roman
Usuario Github: JesusRomanDG
Fecha: 03 de noviembre de 2022
Descripcion: Haciendo uso del sensor KY-020(BALL SWITCH) y un led RGB,
se realiza mediante micropython un programa que detecta la inclinacion.
Si no se detecta inclinacion, el sensor regresa un valor de 0, y se
enciende un led rojo. En cambio, si se detecta inclinacion, el sensor
regresa un valor de 1, entonces se enciende un led verde.
"""

# importando librerias
from machine import Pin
from machine import ADC
import utime

digitalIn = Pin(15, Pin.IN) # inicializando el pin 15 como entrada digital
led = Pin("LED", Pin.OUT) # inicializando el led integrado como salida digital

# inicializando los pines rojo, verde y azul de un led rgb como salidas digitales
red = Pin(2, Pin.OUT)
green = Pin(3, Pin.OUT)

# ciclo
while True:
    
    led.value(1) # enciende el led integrado
    
    lectura = digitalIn.value() # guarda el valor de la entrada digital del sensor Ball Switch
    print(lectura) # imprime el valor obtenido de la lectura
    
    utime.sleep(1) # espera 1 segundo

    # si la lectura digital es igual a 1, entonces enciende el led de color verde y apaga el rojo
    if lectura == 1:
        red.value(0)
        green.value(1)
        
        utime.sleep(1)
    
    # si la lectura digital es igual a 0, entonces enciende el led rojo y apaga el led verde
    if lectura == 0:
        red.value(1)
        green.value(0)
        
        utime.sleep(1)
``
