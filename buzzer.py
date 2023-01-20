import machine
import utime
"""from machine import PWM, Pin
buzzer = PWM(Pin(15))
buzzer.freq(500)
volume = 1000

while True:
    buzzer.duty_u16(volume)"""

led = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(28, machine.Pin.OUT)


led.on()
led2.on()


