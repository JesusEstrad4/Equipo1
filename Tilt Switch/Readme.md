    from machine import Pin
    import time,utime  

    bolitaDMercurio=Pin(15,Pin.IN)  

    while True:
        bolitaDMercurio.value()

        if bolitaDMercurio.value() == 0:
            print("No inclinado")
        elif bolitaDMercurio.value()==1:
            print("Inclinado")
