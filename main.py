import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

led.on()
utime.sleep(0.3)
led.off()

import website