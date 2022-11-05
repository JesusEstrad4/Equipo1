    from machine import Pin
    import time,utime  

    tempDig=Pin(15,Pin.IN)  

    while True:
        tempDig.value()
        print(str(tempDig.value()) +"C")
        utime.sleep(1)
