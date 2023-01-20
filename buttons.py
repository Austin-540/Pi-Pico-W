import machine
import utime
from picozero import Button

led = machine.Pin(28, machine.Pin.OUT)
button = Button(12)

button.when_pressed = led.on()
button.when_released = led.off()

while True:
    pass
