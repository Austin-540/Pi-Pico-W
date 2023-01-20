import machine
from machine import Pin
import utime

led = machine.Pin("LED", machine.Pin.OUT)

led.on()
utime.sleep(0.3)
led.off()

#import website


while True:
    led.toggle()
    utime.sleep(0.5)