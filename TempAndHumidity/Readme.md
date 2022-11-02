from machine import Pin
from dht import DHT12, InvalidChecksum

pin=Pin(16,Pin.IN)

while True:
    utime.sleep(1)
    data_dht=DHT12(pin)
    temp=(data_dht.temperature)
    humidity=(data_dht.humidity)
    print("temperature(C):{}".format(temp))
    print("humidity(%): {}".format(humidity))
