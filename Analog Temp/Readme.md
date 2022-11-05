    from machine import Pin
    import time,utime  

    lector=Pin(15,Pin.IN)  
    factorconversion = 3.3 / 65365

    while True:

        celsius = lector.read_u16() * factorconversion
        temperatura = 27 - (celsius - 0.706) / 0.001721
        print(temperatura)
        utime.sleep(1)
