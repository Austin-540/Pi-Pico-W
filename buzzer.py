import machine
import math
from machine import PWM, Pin
from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.freq(500)
buzzer.duty_u16(1000)




led2 = machine.Pin(28, machine.Pin.OUT)
potentiometer = machine.ADC(26)


while True:
    new_num = math.floor((potentiometer.read_u16()/60)) +50
    print(new_num)
    buzzer.freq(new_num)
    sleep(0.1)
    



