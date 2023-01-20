import machine
from machine import Pin
import utime

led = machine.Pin("LED", machine.Pin.OUT)

led.on()
utime.sleep(0.3)
led.off()

#import website


blue_led = machine.Pin(16, Pin.OUT)

while True:
    blue_led.toggle()
    led.toggle()
    utime.sleep(0.5)