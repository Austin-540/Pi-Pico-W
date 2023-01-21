from machine import Pin

import utime

led_r = machine.Pin(22, machine.Pin.OUT)
led_g = machine.Pin(26, machine.Pin.OUT)
led_b = machine.Pin(27, machine.Pin.OUT)


while True:
    led_b.on()
    led_r.on()
    led_g.on()
