Code:
from machine import Pin
import time

led = Pin(10, Pin.OUT)
button = Pin(1, Pin.IN, Pin.PULL_DOWN)

while True:
if button.value():
led.toggle()
time.sleep(0.5)
print(button.value)

https://www.loom.com/share/69a18eb71bd744588b207ff995c0316c
