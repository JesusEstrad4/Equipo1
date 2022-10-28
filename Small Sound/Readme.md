from machine import Pin
import utime
led=Pin(15,Pin.OUT)  
button=Pin(16,Pin.IN,Pin.PULL_DOWN) 

def led_toggle(irq):
    print('1')
     
button.irq(trigger=Pin.IRQ_RISING,handler=led_toggle)
