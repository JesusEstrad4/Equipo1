```python
"""
Autor: Dominguez Garcia Jesus Roman
Usuario Github: JesusRomanDG
Fecha: 03 de noviembre de 2022
Descripcion: Haciendo uso del sensor KY-039(HEARTBEAT) y un led RGB,
se realiza mediante micropython un programa que enciende el led rojo
del componente RGB cada vez que el sensor de latidos detecta un pulso .
"""

# importando librerias
from machine import Pin
from machine import ADC
import utime

analogIn = ADC(26) # inicializando el pin 26 como entrada analogica
led = Pin("LED", Pin.OUT) # inicializando el led integrado como salida digital

# ciclo
while True:
    
    led.value(1) # enciende el led integrado
    
    lectura = 60000/analogIn.read_u16() # guarda el valor de la entrada analogica del sensor
    print(lectura) # imprime el valor obtenido de la lectura
    
    utime.sleep(1) # espera 1 segundo
```