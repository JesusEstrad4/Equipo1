"""
Omar Gamaliel Rodriguez Moreno
Usuario Barny-Claus
Estudiante del Instituto Tecnológico de Tijuana
  Materia: Sistemas programables
"""

from machine import Pin
import time,utime  

nivel=Pin(15,Pin.IN)  
 
while True:
    nivel.value()
    if nivel.value() == 0:
        print("No está nivelado")
    elif nivel.value()==1:
        print("Está ")
