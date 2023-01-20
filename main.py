import machine
from machine import Pin
import utime

button = Pin(0, Pin.IN, Pin.PULL_UP)   

if button.value() == 0:
    print("Buttons imported")
    import buttons
    

led = machine.Pin("LED", machine.Pin.OUT)

led.on()
utime.sleep(0.3)
led.off()

#import website


while True:
    led.toggle()
    utime.sleep(0.5)