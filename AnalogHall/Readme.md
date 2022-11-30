Analog hall

ky-035



from machine import Pin import utime

sensor = Pin(18, machine.Pin.OUT)

a=1
while True:
    sensor.value(1)
    print(str(a)+ " sensor: "+ str(sensor.value()))
    receptor.value(0)
    utime.sleep(1)
