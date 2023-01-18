import machine
import utime

led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(5):
    led.toggle()
    utime.sleep(1)