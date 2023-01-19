import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

led.on()
print("Line 7 main.py")
utime.sleep(0.3)
led.off()

import website