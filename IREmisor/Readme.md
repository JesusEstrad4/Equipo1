from machine import Pin
import utime

emisor = Pin(18, machine.Pin.OUT)

receptor = Pin(4, machine.Pin.IN)
a=1
while True:
    emisor.value(1)
    print(str(a)+ " Receptor: "+ str(receptor.value()) + " - emisor: "+" "+str(emisor.value()))
    receptor.value(0)
    utime.sleep(1)

